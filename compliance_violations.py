import os
from collections import defaultdict
from dotenv import load_dotenv
from falconpy import OAuth2, Alerts

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

auth = OAuth2(
    client_id=os.environ["FALCON_CLIENT_ID"],
    client_secret=os.environ["FALCON_CLIENT_SECRET"],
    base_url=os.environ.get("FALCON_BASE_URL", "https://api.crowdstrike.com"),
)
falcon = Alerts(auth_object=auth)

print("Fetching alerts...")

# Page through all alert IDs
all_ids = []
offset = 0
while True:
    r = falcon.query_alerts(limit=9999, offset=offset, filter="status:!'closed'")
    if r["status_code"] != 200:
        print(f"Error querying alerts: {r['body']}")
        break
    ids = r["body"].get("resources") or []
    all_ids.extend(ids)
    total = r["body"].get("meta", {}).get("pagination", {}).get("total", 0)
    offset += len(ids)
    if offset >= total or not ids:
        break

print(f"Found {len(all_ids)} alerts. Fetching details...")

# Fetch details in batches of 1000
violation_counts = defaultdict(int)
severity_map = {}

for i in range(0, len(all_ids), 1000):
    batch = all_ids[i:i + 1000]
    r = falcon.get_alerts(ids=batch)
    if r["status_code"] != 200:
        print(f"Error fetching batch: {r['body']}")
        continue
    for resource in r["body"].get("resources") or []:
        title = resource.get("title") or resource.get("name") or "Unknown"
        violation_counts[title] += 1
        if title not in severity_map:
            severity_map[title] = resource.get("severity_name", "")

print(f"\nTop policies/rules by violation count (active alerts):\n")
print(f"{'#':>3}  {'Count':>7}  {'Severity':<10}  Rule/Policy")
print("-" * 80)

sorted_violations = sorted(violation_counts.items(), key=lambda x: x[1], reverse=True)
for rank, (title, count) in enumerate(sorted_violations[:25], 1):
    severity = severity_map.get(title, "")
    print(f"{rank:>3}. {count:>7}  {severity:<10}  {title}")

print("-" * 80)
print(f"\nTotal distinct rules with violations: {len(violation_counts)}")
print(f"Total active violations:              {sum(violation_counts.values())}")
