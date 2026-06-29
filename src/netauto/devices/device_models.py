from __future__ import annotations

from pydantic import BaseModel, Field


class NetworkDevice(BaseModel):
    """Validated device record from the inventory file."""

    name: str
    host: str
    device_type: str = Field(default="cisco_ios")
    username: str | None = None
    password: str | None = None
    secret: str | None = None
    port: int = 22
