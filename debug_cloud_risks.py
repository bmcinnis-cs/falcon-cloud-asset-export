import json
import os
from dotenv import load_dotenv
from falconpy import OAuth2, CloudSecurity, CloudSecurityAssets

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
auth = OAuth2(
    client_id=os.environ["FALCON_CLIENT_ID"],
    client_secret=os.environ["FALCON_CLIENT_SECRET"],
    base_url=os.environ.get("FALCON_BASE_URL", "https://api.crowdstrike.com"),
)
cs = CloudSecurity(auth_object=auth)
csa = CloudSecurityAssets(auth_object=auth)

r = cs.combined_cloud_risks(
    filter="rule_name:['Unused identity','Unused identity has access to sensitive data','Unused identity with excessive permissions']",
    limit=10,
)
risks = r["body"].get("resources") or []
print(f"Found {len(risks)} risk(s). Inspecting first risk fields:")
if risks:
    print(json.dumps({k: v for k, v in risks[0].items() if k in ("asset_id", "asset_name", "asset_gcrn", "crn")}, indent=2))

gcrns = list({risk["asset_gcrn"] for risk in risks if risk.get("asset_gcrn")})
if gcrns:
    print(f"\nCalling get_assets with {len(gcrns)} GCRN(s)...")
    r2 = csa.get_assets(ids=gcrns[:3])
    print(f"Status: {r2['status_code']}")
    assets = r2["body"].get("resources") or []
    if assets:
        print("First asset keys:", list(assets[0].keys()))
        print(json.dumps(assets[0], indent=2))
    else:
        print("No resources returned. Errors:", r2["body"].get("errors"))
