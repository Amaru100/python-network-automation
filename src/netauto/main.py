from __future__ import annotations

import argparse
import logging
from pathlib import Path

from rich.console import Console
from rich.table import Table

from netauto.devices.inventory_loader import InventoryLoadError, load_inventory
from netauto.logging_config import configure_logging


console = Console()
logger = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Cisco network automation toolkit for lab environments."
    )
    parser.add_argument(
        "--inventory",
        default="configs/inventory.example.yml",
        help="Path to the YAML device inventory file.",
    )
    parser.add_argument(
        "--list-devices",
        action="store_true",
        help="Load the inventory and print known devices.",
    )
    return parser


def print_devices(inventory_path: Path) -> None:
    devices = load_inventory(inventory_path)

    table = Table(title="Network Device Inventory")
    table.add_column("Name", style="cyan")
    table.add_column("Host")
    table.add_column("Type")
    table.add_column("Port", justify="right")

    for device in devices:
        table.add_row(device.name, device.host, device.device_type, str(device.port))

    console.print(table)
    logger.info("Loaded %s device(s) from %s", len(devices), inventory_path)


def main() -> int:
    """Application entry point."""
    configure_logging()
    parser = build_parser()
    args = parser.parse_args()

    console.print("[bold green]Python Network Automation[/bold green]")

    if args.list_devices:
        try:
            print_devices(Path(args.inventory))
        except InventoryLoadError as exc:
            logger.error("Inventory loading failed: %s", exc)
            console.print(f"[bold red]Error:[/bold red] {exc}")
            return 1
    else:
        console.print("Use --list-devices to validate and display the inventory.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
