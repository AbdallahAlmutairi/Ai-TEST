"""Utility helpers for consistent JSON responses."""

from __future__ import annotations

from typing import Any, Dict, Tuple


def success(data: Dict[str, Any], status: int = 200) -> Tuple[Dict[str, Any], int]:
    """Return a successful JSON response."""

    return data, status


def error(message: str, status: int = 400) -> Tuple[Dict[str, str], int]:
    """Return an error JSON response with ``message``."""

    return {"error": message}, status


__all__ = ["success", "error"]

