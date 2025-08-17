"""Generate trading signals from model probabilities and indicators."""
from __future__ import annotations

from typing import List


def prob_to_action(prob: float) -> str:
    """Convert probability of upward move to discrete action."""
    if prob > 0.55:
        return "Buy"
    if prob < 0.45:
        return "Sell"
    return "Hold"


def generate_reasons(indicators: dict, locale: str = "en") -> List[str]:
    """Basic indicator-based rationale."""
    reasons: List[str] = []
    rsi = indicators.get("rsi")
    if rsi is not None:
        if rsi < 30:
            reasons.append("RSI indicates oversold" if locale == "en" else "مؤشر القوة النسبية في منطقة بيع مفرط")
        elif rsi > 70:
            reasons.append("RSI indicates overbought" if locale == "en" else "مؤشر القوة النسبية في منطقة شراء مفرط")
    bb = indicators.get("bollinger_b")
    if bb is not None:
        if bb > 1:
            reasons.append("Price near upper Bollinger band" if locale == "en" else "السعر قرب الحد العلوي لبولينجر")
        elif bb < 0:
            reasons.append("Price near lower Bollinger band" if locale == "en" else "السعر قرب الحد السفلي لبولينجر")
    return reasons
