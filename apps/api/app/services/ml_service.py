"""Utilities for interacting with the internal AI service."""

from __future__ import annotations

from typing import Any, Dict, Iterable, List

from ai_service.app.models import infer
from ai_service.app.backtest.engine import run_backtest as _run_backtest


def analyze(ticker: str) -> Dict[str, Any]:
    """Analyse *ticker* and return the raw response from ``ai_service``."""

    return infer.analyze(ticker)


def predict(ticker: str) -> str:
    """Return only the high level action for convenience."""

    return analyze(ticker)["action"]


def batch_signals(symbols: Iterable[str]) -> List[Dict[str, Any]]:
    """Return analyses for multiple symbols."""

    return [analyze(sym) for sym in symbols]


def backtest(ticker: str) -> Dict[str, Any]:
    """Run a backtest for *ticker* using the AI service engine."""

    metrics, equity, trades = _run_backtest(ticker)
    return {"metrics": metrics, "equity": equity, "trades": trades}


__all__ = ["analyze", "predict", "batch_signals", "backtest"]

