# Python Network Automation

Professional Cisco network automation project for a networking graduate portfolio.

## Current Scope

This project currently supports loading and validating a Cisco device inventory from YAML. Real Cisco SSH automation will be added after the Cisco Packet Tracer lab devices are configured for SSH.

## Features Planned

- Connect to Cisco devices using SSH
- Backup running configurations
- Configure VLANs
- Configure interfaces
- Run device health checks
- Generate reports
- Structured logging

## Architecture

```mermaid
flowchart TD
    A[CLI Entry Point] --> B[Service Layer]
    B --> C[SSH Connection Layer]
    B --> D[Inventory Loader]
    B --> E[Report Generator]
    C --> F[Cisco Devices via SSH]
    D --> G[YAML Inventory Files]
    E --> H[Markdown / Text Reports]
    B --> I[Logging System]
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
pip install -e .
```

Copy the environment template:

```powershell
Copy-Item .env.example .env
```

Run the application:

```powershell
python -m netauto.main
```

Validate and display the sample inventory:

```powershell
python -m netauto.main --list-devices
```

Run tests:

```powershell
pytest
```

## Docker

Build and run with Docker Compose:

```powershell
docker compose up --build
```

## Packet Tracer Lab

No real devices are configured yet. The sample inventory in `configs/inventory.example.yml` uses placeholder IP addresses that we will align with the Packet Tracer topology later.

## What The Inventory Feature Does

The inventory loader reads devices from YAML, expands environment variable placeholders such as `${NETAUTO_DEFAULT_PASSWORD}`, and validates each device before any SSH connection is attempted.

This matters because automation should fail early if the source data is wrong. A bad IP address, missing hostname, or malformed inventory should be caught before the tool starts changing network devices.

## Troubleshooting

- If Python cannot find `netauto`, run commands from the project root directory.
- If `python -m netauto.main` fails, confirm you ran `pip install -e .` inside the active virtual environment.
- If SSH fails later, confirm the Cisco device has an IP address, SSH enabled, a local user, and reachable routing.
- Never commit `.env`; use `.env.example` for safe placeholders.

## Future Improvements

- Add Netmiko SSH connection handling
- Add configuration backup service
- Add VLAN configuration workflow
- Add interface configuration workflow
- Add health checks and report generation
- Add GitHub Actions CI
