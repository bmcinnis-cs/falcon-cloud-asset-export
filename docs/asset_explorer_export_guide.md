# Asset Explorer CSV Export — Setup & Usage Guide

Scripts covered:
- `azure_unmanaged_vms_export.py` — Unmanaged, Azure, running instances
- `aws_unmanaged_vms_export.py` — Unmanaged, AWS, running instances

---

## 1. Install Python

Both scripts require **Python 3.8 or later**.

### macOS

```bash
# Option A — Homebrew (recommended)
brew install python

# Option B — download the installer from python.org
# https://www.python.org/downloads/macos/
```

### Windows

1. Download the installer from **https://www.python.org/downloads/windows/**
2. Run the installer and check **"Add Python to PATH"** before clicking Install
3. Verify in a new terminal:

```powershell
python --version
```

### Linux (Debian / Ubuntu)

```bash
sudo apt update && sudo apt install python3 python3-pip -y
python3 --version
```

---

## 2. Install Dependencies

From the root of this repository, run:

```bash
pip install crowdstrike-falconpy python-dotenv
```

| Package | Purpose |
|---|---|
| `crowdstrike-falconpy` | FalconPy SDK — wraps the CrowdStrike Falcon APIs |
| `python-dotenv` | Loads API credentials from a `.env` file |

---

## 3. Configure API Credentials

### 3a. Create a Falcon API Client

1. Log in to the Falcon console
2. Navigate to **Support & Resources → API Clients and Keys**
3. Click **Add new API client**
4. Give it a descriptive name (e.g. `Asset Explorer Export`)
5. Under **Scope**, enable the following permission:

| Scope | Access |
|---|---|
| **Cloud Security Assets** | Read |

6. Click **Add** and copy the **Client ID** and **Client Secret** — the secret is only shown once

### 3b. Create a `.env` File

Create a file named `.env` in the root of this repository:

```ini
FALCON_CLIENT_ID=your_client_id_here
FALCON_CLIENT_SECRET=your_client_secret_here

# Optional — only needed for non-US-1 clouds
# FALCON_BASE_URL=https://api.laggar.gcw.crowdstrike.com   # US-GOV-1
# FALCON_BASE_URL=https://api.eu-1.crowdstrike.com         # EU-1
# FALCON_BASE_URL=https://api.us-2.crowdstrike.com         # US-2
```

> **Note:** `.env` is listed in `.gitignore`. Never commit credentials to source control.

---

## 4. Run the Scripts

### Export Azure Unmanaged Running VMs

```bash
python azure_unmanaged_vms_export.py
```

Output file: `azure_unmanaged_running_vms.csv`

### Export AWS Unmanaged Running VMs

```bash
python aws_unmanaged_vms_export.py
```

Output file: `aws_unmanaged_running_vms.csv`

Both scripts print progress to the terminal:

```
Querying: managed_by:'Unmanaged'+cloud_provider:'azure'+instance_state:'running'
Found 342 asset ID(s). Fetching details...
Wrote 342 row(s) to azure_unmanaged_running_vms.csv
```

---

## 5. CSV Output

Each row is one cloud asset. Top-level fields (e.g. `resource_name`, `region`, `account_id`) are written as plain values. Nested objects (e.g. `cloud_risks`, `tags`) are serialized as JSON strings within their column.

Useful columns to look for:

| Column | Description |
|---|---|
| `resource_name` | Asset name |
| `resource_type_name` | e.g. Virtual Machine |
| `account_id` | Cloud account / subscription ID |
| `region` | Cloud region |
| `instance_state` | Running state |
| `managed_by` | Sensor management status |
| `first_seen` | When the asset was first discovered |
| `updated_at` | Last update timestamp |
| `publicly_exposed` | Whether the asset is internet-exposed |
| `cloud_risks` | Associated cloud risk detections (JSON) |

---

## 6. Troubleshooting

### Script returns "No assets found matching the filter"

FQL values are **case-sensitive** and must match exactly what the platform stores. If you get zero results, try adjusting the `FILTER` constant at the top of the script:

| Field | Try these values |
|---|---|
| `cloud_provider` | `'azure'` · `'Azure'` · `'aws'` · `'AWS'` |
| `instance_state` | `'running'` · `'VM running'` |
| `managed_by` | `'Unmanaged'` · `'unmanaged'` |

### Authentication errors (401)

- Confirm **Client ID** and **Client Secret** are correct in `.env`
- Confirm the API client has **Cloud Security Assets: Read** scope enabled
- If your tenant is not on US-1, set `FALCON_BASE_URL` in `.env`

### `ModuleNotFoundError: No module named 'falconpy'`

The dependencies are not installed in the Python environment you are running. Re-run:

```bash
pip install crowdstrike-falconpy python-dotenv
```

If you use multiple Python versions, make sure you install into the same environment you use to run the scripts (e.g. use `pip3` or a virtual environment).
