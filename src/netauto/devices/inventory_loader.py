from __future__ import annotations

import os
from pathlib import Path

import yaml
from pydantic import ValidationError

from netauto.devices.device_models import NetworkDevice


class InventoryLoadError(RuntimeError):
    """Raised when the inventory file cannot be loaded or validated."""


def _expand_env_vars(value: object) -> object:
    if isinstance(value, str):
        return os.path.expandvars(value)
    if isinstance(value, list):
        return [_expand_env_vars(item) for item in value]
    if isinstance(value, dict):
        return {key: _expand_env_vars(item) for key, item in value.items()}
    return value


def load_inventory(path: str | Path) -> list[NetworkDevice]:
    """Load and validate network devices from a YAML inventory file."""
    inventory_path = Path(path)

    if not inventory_path.exists():
        raise InventoryLoadError(f"Inventory file not found: {inventory_path}")

    try:
        with inventory_path.open("r", encoding="utf-8") as file:
            raw_data = yaml.safe_load(file) or {}
    except yaml.YAMLError as exc:
        raise InventoryLoadError(f"Invalid YAML in inventory: {inventory_path}") from exc

    raw_data = _expand_env_vars(raw_data)

    devices = raw_data.get("devices", [])

    if not isinstance(devices, list):
        raise InventoryLoadError("Inventory field 'devices' must be a list.")

    try:
        return [NetworkDevice.model_validate(device) for device in devices]
    except ValidationError as exc:
        raise InventoryLoadError("Inventory contains invalid device records.") from exc
