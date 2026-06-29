# Architecture

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

## Design Decisions

- The CLI is separated from the service layer so user interaction does not get mixed with network automation logic.
- SSH access will live behind a connection adapter so Netmiko-specific code is isolated.
- Inventory is stored in YAML so devices can be changed without editing Python code.
- Secrets belong in `.env`, not in Git-tracked files.
- Backups and reports are generated into dedicated folders and ignored by Git by default.
