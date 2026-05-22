import os
from dotenv import load_dotenv
from falconpy import OAuth2, CloudSecurity

UNUSED_IDENTITY_RULES = [
    "Unused identity",
    "Unused identity has access to sensitive data",
    "Unused identity with excessive permissions",
]


def get_unused_identities(cs):
    names = []
    offset = 0
    fql = "rule_name:['" + "','".join(UNUSED_IDENTITY_RULES) + "']+status:'Open'"
    while True:
        r = cs.combined_cloud_risks(filter=fql, limit=500, offset=offset)
        if r["status_code"] != 200:
            print(f"Error: {r['body']}")
            break
        resources = r["body"].get("resources") or []
        for risk in resources:
            name = risk.get("asset_id", "")
            if name:
                names.append(name)
        total = r["body"].get("meta", {}).get("pagination", {}).get("total", 0)
        offset += len(resources)
        if offset >= total or not resources:
            break
    return names


if __name__ == "__main__":
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    auth = OAuth2(
        client_id=os.environ["FALCON_CLIENT_ID"],
        client_secret=os.environ["FALCON_CLIENT_SECRET"],
        base_url=os.environ.get("FALCON_BASE_URL", "https://api.crowdstrike.com"),
    )
    cs = CloudSecurity(auth_object=auth)

    names = get_unused_identities(cs)

    print(f"Unused Identity assets ({len(names)} total):\n")
    for name in sorted(set(names)):
        print(f"  {name}")
