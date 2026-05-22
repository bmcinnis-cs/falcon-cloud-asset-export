# Falcon Cloud Asset Export

> Python scripts for exporting unmanaged running VM data from [CrowdStrike Falcon Cloud Security](https://www.crowdstrike.com/platform/cloud-security/) using the [FalconPy SDK](https://github.com/CrowdStrike/falconpy).

---

## Scripts

All scripts query the Falcon Asset Explorer for instances that are **unmanaged** (no CrowdStrike sensor) and currently **running**.

| Script | Cloud | Columns | Output File |
|---|---|---|---|
| `azure_unmanaged_vms_export.py` | Azure | All fields | `azure_unmanaged_running_vms.csv` |
| `aws_unmanaged_vms_export.py` | AWS | All fields | `aws_unmanaged_running_vms.csv` |
| `azure_unmanaged_vms_summary.py` | Azure | `instance_id`, `account_id` | `azure_unmanaged_running_vms_summary.csv` |
| `aws_unmanaged_vms_summary.py` | AWS | `instance_id`, `account_id` | `aws_unmanaged_running_vms_summary.csv` |

---

## Prerequisites

- Python 3.8+
- A CrowdStrike Falcon API client with the **Cloud Security Assets: Read** scope

See [docs/asset_explorer_export_guide.md](docs/asset_explorer_export_guide.md) for step-by-step instructions on installing Python, creating an API client, and configuring credentials.

---

## Quick Start

**1. Create and activate a virtual environment**

```bash
python -m venv .venv
```

| Platform | Activation command |
|---|---|
| macOS / Linux | `source .venv/bin/activate` |
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |

You'll see `(.venv)` in your terminal prompt once active. You need to activate the virtual environment each time you open a new terminal session before running the scripts.

**2. Install dependencies**

```bash
pip install crowdstrike-falconpy python-dotenv
```

**2. Configure credentials**

```bash
cp .env.example .env
```

Edit `.env` with your Falcon API Client ID and Secret:

```ini
FALCON_CLIENT_ID=your_client_id_here
FALCON_CLIENT_SECRET=your_client_secret_here
```

**3. Run**

```bash
python azure_unmanaged_vms_export.py
python aws_unmanaged_vms_export.py
```

---

## Output

Each script produces a CSV file where every row is one cloud asset. Nested fields (e.g. `cloud_risks`, `tags`) are serialized as JSON strings within their column.

Key columns include: `resource_name`, `account_id`, `region`, `instance_state`, `managed_by`, `publicly_exposed`, `first_seen`, `updated_at`.

---

## Documentation

Full setup and troubleshooting guide: [docs/asset_explorer_export_guide.md](docs/asset_explorer_export_guide.md)
