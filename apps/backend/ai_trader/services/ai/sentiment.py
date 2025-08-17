"""Tiny sentiment scoring utility used for examples and tests."""

from __future__ import annotations

from typing import Iterable

POSITIVE = {"good", "great", "positive", "up", "gain"}
NEGATIVE = {"bad", "poor", "negative", "down", "loss"}


def score_headlines(headlines: Iterable[str]) -> float:
    """Return a sentiment score between -1 and 1.

    The implementation is intentionally simple – it counts occurrences of
    predefined positive and negative words.  The result is normalised to the
    ``[-1, 1]`` range so callers can interpret it as a confidence-like value.
    """

    pos = neg = 0
    for hl in headlines:
        words = {w.lower() for w in hl.split()}
        pos += len(words & POSITIVE)
        neg += len(words & NEGATIVE)
    total = pos + neg
    if total == 0:
        return 0.0
    return (pos - neg) / total


__all__ = ["score_headlines"]

