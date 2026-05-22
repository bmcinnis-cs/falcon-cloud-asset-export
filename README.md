# Falcon Cloud Asset Export

> Python scripts for exporting unmanaged running VM data from [CrowdStrike Falcon Cloud Security](https://www.crowdstrike.com/platform/cloud-security/) using the [FalconPy SDK](https://github.com/CrowdStrike/falconpy).

---

## Scripts

All scripts query the Falcon Asset Explorer for instances that are **unmanaged** (no CrowdStrike sensor) and currently **running**, outputting two columns: `resource_id` and `account_id`.

| Script | Cloud | Output File |
|---|---|---|
| `azure_unmanaged_vms_export.py` | Azure | `azure_unmanaged_running_vms.csv` |
| `aws_unmanaged_vms_export.py` | AWS | `aws_unmanaged_running_vms.csv` |
| `gcp_unmanaged_vms_export.py` | GCP | `gcp_unmanaged_running_vms.csv` |

---

## Prerequisites

- Python 3.8+
- CrowdStrike Falcon API client with **Cloud Security Assets: Read** scope

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

**3. Configure credentials**

```bash
cp .env.example .env
```

Edit `.env` with your Falcon API Client ID and Secret:

```ini
FALCON_CLIENT_ID=your_client_id_here
FALCON_CLIENT_SECRET=your_client_secret_here
```

**4. Run**

```bash
python azure_unmanaged_vms_export.py
python aws_unmanaged_vms_export.py
python gcp_unmanaged_vms_export.py
```

---

## Output

Each script produces a CSV with two columns per asset:

| Column | Description |
|---|---|
| `resource_id` | The cloud resource identifier for the VM |
| `account_id` | The cloud account / subscription the VM belongs to |

> **Note:** If opening in Excel, use **Data → From Text/CSV** and set `account_id` to **Text** type during import to prevent large account IDs from being displayed in scientific notation.

---

## Documentation

Full setup and troubleshooting guide: [docs/asset_explorer_export_guide.md](docs/asset_explorer_export_guide.md)
