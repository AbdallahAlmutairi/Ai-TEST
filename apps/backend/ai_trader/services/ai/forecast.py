"""Forecasting utilities that wrap the AI service."""

from __future__ import annotations

from typing import Dict

from ai_service.app.models import infer


def predict(symbol: str) -> Dict[str, object]:
    """Return a prediction dictionary for ``symbol``.

    This function acts as a very small client around the local
    :mod:`ai_service` package used in the tests.  It returns a dictionary with
    the keys expected by the Flask routes.
    """

    res = infer.analyze(symbol)
    return {
        "symbol": symbol,
        "direction": res["action"],
        "target": None,
        "confidence": res["confidence"],
        "rationale": res["reasons"],
        "disclaimer": res["disclaimer"],
    }


__all__ = ["predict"]

