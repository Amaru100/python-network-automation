from pathlib import Path

from netauto.devices.inventory_loader import load_inventory


def test_load_inventory_reads_devices(tmp_path: Path) -> None:
    inventory = tmp_path / "inventory.yml"
    inventory.write_text(
        """
devices:
  - name: SW1
    host: 192.168.10.11
""",
        encoding="utf-8",
    )

    devices = load_inventory(inventory)

    assert len(devices) == 1
    assert devices[0].name == "SW1"
