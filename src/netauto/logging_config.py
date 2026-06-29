from __future__ import annotations

import logging

from netauto.config import settings


def configure_logging() -> None:
    """Configure application-wide logging."""
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
