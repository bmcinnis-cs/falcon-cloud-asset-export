import csv
import os
from dotenv import load_dotenv
from falconpy import OAuth2, CloudSecurity, CloudSecurityAssets

BASE_FILTER = "managed_by:'Unmanaged'+cloud_provider:'aws'+instance_state:'running'"
OUTPUT_FILE = "aws_unmanaged_running_vms.csv"


def resolve_group_fql(cs_sdk, name):
    r = cs_sdk.list_group_ids(filter=f"name:'{name}'")
    group_ids = r["body"].get("resources") or []
    if not group_ids:
        raise RuntimeError(f"Cloud group '{name}' not found.")
    r2 = cs_sdk.list_cloud_groups_by_id(ids=group_ids)
    group = (r2["body"].get("resources") or [{}])[0]
    terms = []
    for selector in (group.get("selectors") or {}).get("cloud_resources") or []:
        account_ids = selector.get("account_ids") or []
        if account_ids:
            joined = ",".join(f"'{a}'" for a in account_ids)
            terms.append(f"account_id:[{joined}]")
        for tag_str in (selector.get("filters") or {}).get("tags") or []:
            if "=" in tag_str:
                key, _, value = tag_str.partition("=")
                terms.append(f"tag_key:'{key}'")
                terms.append(f"tag_value:'{value}'")
            else:
                terms.append(f"tag_key:'{tag_str}'")
    return terms


def build_filter(group_terms=None):
    f = BASE_FILTER
    tag_key = os.environ.get("FALCON_CLOUD_TAG_KEY")
    if tag_key:
        f += f"+tag_key:'{tag_key}'"
    tag_value = os.environ.get("FALCON_CLOUD_TAG_VALUE")
    if tag_value:
        f += f"+tag_value:'{tag_value}'"
    if group_terms:
        f += "+" + "+".join(group_terms)
    return f


def query_all_ids(sdk, fql):
    ids = []
    after = None
    while True:
        params = {"limit": 1000, "filter": fql}
        if after:
            params["after"] = after
        r = sdk.query_assets(**params)
        if r["status_code"] != 200:
            raise RuntimeError(f"query_assets failed: {r['body'].get('errors')}")
        batch = r["body"].get("resources") or []
        ids.extend(batch)
        after = r["body"].get("meta", {}).get("pagination", {}).get("after")
        if not batch or not after:
            break
    return ids


def fetch_assets(sdk, ids):
    assets = []
    for i in range(0, len(ids), 100):
        r = sdk.get_assets(ids=ids[i:i + 100])
        if r["status_code"] != 200:
            raise RuntimeError(f"get_assets failed: {r['body'].get('errors')}")
        assets.extend(r["body"].get("resources") or [])
    return assets


def write_csv(assets):
    if not assets:
        print("No assets found matching the filter.")
        return
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["resource_id", "account_id"])
        writer.writeheader()
        for asset in assets:
            writer.writerow({
                "resource_id": asset.get("resource_id", ""),
                "account_id": "\t" + str(asset.get("account_id", "")),
            })
    print(f"Wrote {len(assets)} row(s) to {OUTPUT_FILE}")


if __name__ == "__main__":
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    auth = OAuth2(
        client_id=os.environ["FALCON_CLIENT_ID"],
        client_secret=os.environ["FALCON_CLIENT_SECRET"],
        base_url=os.environ.get("FALCON_BASE_URL", "https://api.crowdstrike.com"),
    )
    csa = CloudSecurityAssets(auth_object=auth)

    group_terms = []
    group = os.environ.get("FALCON_CLOUD_GROUP")
    if group:
        cs = CloudSecurity(auth_object=auth)
        group_terms = resolve_group_fql(cs, group)
        print(f"Group '{group}' resolved to FQL terms: {group_terms}")

    fql = build_filter(group_terms)
    print(f"Querying: {fql}")
    ids = query_all_ids(csa, fql)
    print(f"Found {len(ids)} asset ID(s). Fetching details...")
    assets = fetch_assets(csa, ids)
    write_csv(assets)
