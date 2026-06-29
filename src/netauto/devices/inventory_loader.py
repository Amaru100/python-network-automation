from __future__ import annotations

from pathlib import Path

import yaml

from netauto.devices.device_models import NetworkDevice


def load_inventory(path: Path) -> list[NetworkDevice]:
    """Load and validate network devices from a YAML inventory file."""
    with path.open("r", encoding="utf-8") as file:
        raw_data = yaml.safe_load(file) or {}

    devices = raw_data.get("devices", [])
    return [NetworkDevice.model_validate(device) for device in devices]
