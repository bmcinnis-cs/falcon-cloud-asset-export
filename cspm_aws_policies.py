import os
from dotenv import load_dotenv
from falconpy import OAuth2, CloudPolicies

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

auth = OAuth2(
    client_id=os.environ["FALCON_CLIENT_ID"],
    client_secret=os.environ["FALCON_CLIENT_SECRET"],
    base_url=os.environ.get("FALCON_BASE_URL", "https://api.crowdstrike.com"),
)
cp = CloudPolicies(auth_object=auth)

print("Fetching AWS CSPM policies...")

# Page through all AWS rule IDs
all_ids = []
offset = 0
while True:
    r = cp.query_rule(limit=500, offset=offset, filter="rule_provider:'AWS'")
    if r["status_code"] != 200:
        print(f"Error: {r['body']}")
        break
    ids = r["body"].get("resources") or []
    all_ids.extend(ids)
    total = r["body"]["meta"]["pagination"]["total"]
    offset += len(ids)
    if offset >= total or not ids:
        break

print(f"Found {len(all_ids)} AWS policies. Fetching details...\n")

# Fetch details in batches of 500
policies = []
for i in range(0, len(all_ids), 500):
    batch = all_ids[i:i + 500]
    r = cp.get_rule(ids=batch)
    if r["status_code"] != 200:
        print(f"Error fetching batch: {r['body']}")
        continue
    policies.extend(r["body"].get("resources") or [])

# Sort by short_code (numeric ID)
policies.sort(key=lambda x: x.get("short_code", 0))

print(f"{'ID':>6}  {'Severity':<12}  {'Category':<20}  Policy Name")
print("-" * 100)
for p in policies:
    policy_id = p.get("short_code", "N/A")
    name = p.get("name", "Unknown")
    severity = {0: "Informational", 1: "Low", 2: "Medium", 3: "High", 4: "Critical"}.get(p.get("severity"), str(p.get("severity")))
    category = p.get("category", "")
    print(f"{policy_id:>6}  {severity:<12}  {category:<20}  {name}")

print("-" * 100)
print(f"\nTotal AWS CSPM policies: {len(policies)}")
