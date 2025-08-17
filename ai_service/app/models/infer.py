"""Model inference utilities."""
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

import numpy as np

from ..config import get_settings
from ..data.csv_source import CSVSource
from ..features import featurizer
from ..signals.generator import prob_to_action
from ..signals.explain import build_reasons
from .model_store import load_model, MODEL_VERSION

settings = get_settings()


def analyze(
    symbol: str,
    start: Optional[str] = None,
    end: Optional[str] = None,
    interval: str = "1d",
    locale: str = "en",
) -> Dict[str, Any]:
    """Return prediction and indicators for the given symbol."""
    source = CSVSource()
    df = source.get_ohlcv(symbol, start=start, end=end, interval=interval)
    features, _ = featurizer.build_matrix(df)
    model_bundle = load_model()
    model = model_bundle["model"]
    scaler = model_bundle["scaler"]
    last_features = features.iloc[[-1]]
    X = scaler.transform(last_features)
    prob = float(model.predict_proba(X)[0, 1])
    action = prob_to_action(prob)
    confidence = prob if action == "Buy" else 1 - prob if action == "Sell" else abs(prob - 0.5) * 2
    indicators = last_features.iloc[0].to_dict()
    price = float(df["Close"].iloc[-1])
    reasons = build_reasons(df.iloc[-1], last_features.iloc[-1], locale)
    return {
        "symbol": symbol,
        "price": price,
        "action": action,
        "confidence": float(confidence),
        "horizon": "1D",
        "reasons": reasons,
        "indicators": indicators,
        "timestamp": datetime.utcnow(),
        "model_version": MODEL_VERSION,
        "disclaimer": (
            "For research and education only. Not financial advice."
            if locale != "ar"
            else "لأغراض البحث والتعليم فقط. ليست نصيحة استثمارية."
        ),
    }
