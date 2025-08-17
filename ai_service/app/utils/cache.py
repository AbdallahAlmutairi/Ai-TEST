"""Simple in-memory cache used for tests (Redis optional)."""
from __future__ import annotations

from functools import lru_cache
from typing import Any, Callable


def cache(ttl_seconds: int = 300) -> Callable:
    """Decorator providing simple memoisation with LRU cache."""

    def decorator(func: Callable) -> Callable:
        cached = lru_cache(maxsize=32)(func)
        return cached

    return decorator
