"""Caching extension instance."""

from flask_caching import Cache

# Simple in-memory cache suitable for unit tests and small demos.
cache = Cache(config={"CACHE_TYPE": "SimpleCache"})

__all__ = ["cache"]

