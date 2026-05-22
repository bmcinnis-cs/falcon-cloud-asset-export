import csv
import os
from dotenv import load_dotenv
from falconpy import OAuth2, CloudSecurityAssets

FILTER = "managed_by:'Unmanaged'+cloud_provider:'gcp'+instance_state:'running'"
OUTPUT_FILE = "gcp_unmanaged_running_vms.csv"


def query_all_ids(sdk):
    ids = []
    after = None
    while True:
        params = {"limit": 1000, "filter": FILTER}
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
    sdk = CloudSecurityAssets(auth_object=auth)

    print(f"Querying: {FILTER}")
    ids = query_all_ids(sdk)
    print(f"Found {len(ids)} asset ID(s). Fetching details...")
    assets = fetch_assets(sdk, ids)
    write_csv(assets)
