"""Time utilities."""
from __future__ import annotations

from datetime import datetime


def utcnow() -> datetime:
    """Return current UTC time."""
    return datetime.utcnow()
