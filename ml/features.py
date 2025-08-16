"""Feature engineering helpers."""

from typing import List


def compute_moving_average(prices: List[float]) -> float:
    """Return the mean of the price list."""
    if not prices:
        raise ValueError("prices list must not be empty")
    return sum(prices) / len(prices)
