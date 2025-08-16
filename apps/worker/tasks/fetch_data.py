"""Dummy task that pretends to fetch market data."""

import requests


def fetch(symbol: str) -> dict:
    """Return placeholder data for a symbol."""
    _ = requests.Session()
    return {"symbol": symbol}
