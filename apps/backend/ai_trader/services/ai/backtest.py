"""Wrapper around the AI service backtesting engine."""

from __future__ import annotations

from typing import Dict, List

from ai_service.app.backtest.engine import run_backtest as _run_backtest


def run_backtest(symbol: str) -> Dict[str, object]:
    """Execute a simple backtest for ``symbol`` and return the results."""

    metrics, equity, trades = _run_backtest(symbol)
    return {
        "metrics": metrics,
        "equity": equity,
        "trades": trades,
    }


__all__ = ["run_backtest"]

