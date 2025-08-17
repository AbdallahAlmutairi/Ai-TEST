"""Lightweight input validation helpers."""

from __future__ import annotations

import re
from typing import Iterable, List

_SYMBOL_RE = re.compile(r"^[A-Z0-9.]{1,10}$")


def is_valid_symbol(symbol: str) -> bool:
    """Return ``True`` if *symbol* looks like a stock ticker."""

    return bool(_SYMBOL_RE.match(symbol or ""))


def required_fields(data: dict, fields: Iterable[str]) -> List[str]:
    """Return a list of missing keys from *data* given an iterable of
    required field names."""

    return [f for f in fields if not data.get(f)]


__all__ = ["is_valid_symbol", "required_fields"]

