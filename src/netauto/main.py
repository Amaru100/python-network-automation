from __future__ import annotations

from rich.console import Console


console = Console()


def main() -> None:
    """Application entry point."""
    console.print("[bold green]Python Network Automation[/bold green]")
    console.print("Initial project scaffold is ready.")


if __name__ == "__main__":
    main()
