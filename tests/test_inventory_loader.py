import pytest

from netauto.devices.inventory_loader import InventoryLoadError, load_inventory


def test_load_inventory_reads_example_devices() -> None:
    devices = load_inventory("configs/inventory.example.yml")

    assert len(devices) == 2
    assert devices[0].name == "SW1"


def test_load_inventory_raises_for_missing_file() -> None:
    with pytest.raises(InventoryLoadError, match="Inventory file not found"):
        load_inventory("configs/missing.yml")
