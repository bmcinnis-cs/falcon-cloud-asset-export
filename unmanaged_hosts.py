import os
from dotenv import load_dotenv
from falconpy import OAuth2, Discover

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

auth = OAuth2(
    client_id=os.environ["FALCON_CLIENT_ID"],
    client_secret=os.environ["FALCON_CLIENT_SECRET"],
    base_url=os.environ.get("FALCON_BASE_URL", "https://api.crowdstrike.com"),
)
falcon = Discover(auth_object=auth)

def get_host_count(filter_str):
    r = falcon.query_hosts(limit=1, filter=filter_str)
    if r["status_code"] != 200:
        return None, r["body"].get("errors")
    return r["body"]["meta"]["pagination"]["total"], None

total, err = get_host_count(None)
unmanaged, err2 = get_host_count("entity_type:'unmanaged'")
managed, _ = get_host_count("entity_type:'managed'")
unsupported, _ = get_host_count("entity_type:'unsupported'")

print("CrowdStrike Discover — Host Coverage Summary")
print("=" * 45)
print(f"  Unmanaged (no sensor):  {unmanaged or 0:>8,}")
print(f"  Managed (sensor active): {managed or 0:>7,}")
print(f"  Unsupported:             {unsupported or 0:>7,}")
print(f"  Total discovered:        {total or 0:>7,}")
print("=" * 45)

if total and unmanaged is not None:
    pct = (unmanaged / total) * 100
    print(f"\n  {pct:.1f}% of discovered hosts have no sensor")
