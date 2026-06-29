from __future__ import annotations

import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Runtime settings loaded from environment variables."""

    log_level: str = os.getenv("NETAUTO_LOG_LEVEL", "INFO")
    default_username: str | None = os.getenv("NETAUTO_DEFAULT_USERNAME")
    default_password: str | None = os.getenv("NETAUTO_DEFAULT_PASSWORD")
    default_secret: str | None = os.getenv("NETAUTO_DEFAULT_SECRET")


settings = Settings()
