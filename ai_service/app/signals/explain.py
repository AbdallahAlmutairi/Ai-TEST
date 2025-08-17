"""Explain signals combining indicators and model insights."""
from __future__ import annotations

from typing import List

import pandas as pd

from .generator import generate_reasons


def build_reasons(row: pd.Series, indicators: pd.Series, locale: str = "en") -> List[str]:
    reasons = generate_reasons(indicators.to_dict(), locale)
    price = row["Close"]
    ema20 = row.get("ema_20")
    if ema20 is not None:
        if price > ema20:
            reasons.append("Price above EMA20" if locale == "en" else "السعر فوق المتوسط المتحرك 20")
        else:
            reasons.append("Price below EMA20" if locale == "en" else "السعر تحت المتوسط المتحرك 20")
    macd = row.get("macd")
    macd_signal = row.get("macd_signal")
    if macd is not None and macd_signal is not None:
        if macd > macd_signal:
            reasons.append("MACD bullish" if locale == "en" else "تقاطع ماكد إيجابي")
        else:
            reasons.append("MACD bearish" if locale == "en" else "تقاطع ماكد سلبي")
    # ensure at least three bullets
    while len(reasons) < 3:
        reasons.append("Neutral signal" if locale == "en" else "إشارة حيادية")
    return reasons[:6]
