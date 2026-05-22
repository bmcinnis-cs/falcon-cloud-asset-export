# Falcon Cloud Asset Export

Python scripts for exporting cloud security asset data from the CrowdStrike Falcon platform using the [FalconPy SDK](https://github.com/CrowdStrike/falconpy).

## Scripts

| Script | Description | Output |
|---|---|---|
| `azure_unmanaged_vms_export.py` | Unmanaged running VMs — Azure | `azure_unmanaged_running_vms.csv` |
| `aws_unmanaged_vms_export.py` | Unmanaged running VMs — AWS | `aws_unmanaged_running_vms.csv` |

## Setup & Usage

See [docs/asset_explorer_export_guide.md](docs/asset_explorer_export_guide.md) for full setup instructions including:

- Python installation (macOS, Windows, Linux)
- Installing dependencies
- Creating a Falcon API client with the correct scopes
- Configuring credentials
- Running the scripts
- Troubleshooting

## Quick Start

```bash
pip install crowdstrike-falconpy python-dotenv
cp .env.example .env
# Edit .env with your Falcon API credentials
python azure_unmanaged_vms_export.py
python aws_unmanaged_vms_export.py
```

## Required API Scopes

| Scope | Access |
|---|---|
| Cloud Security Assets | Read |
