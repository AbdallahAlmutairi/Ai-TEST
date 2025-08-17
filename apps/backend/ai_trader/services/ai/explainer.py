"""Simple explainability helpers."""

from __future__ import annotations

from typing import List

from ai_service.app.signals.explain import build_reasons
import pandas as pd


def explain(prediction: dict) -> List[str]:
    """Generate human readable reasons from a prediction dictionary."""

    price = prediction.get("price", 0.0)
    indicators = prediction.get("indicators", {})
    return build_reasons(pd.Series({"Close": price}), pd.Series(indicators))


__all__ = ["explain"]

