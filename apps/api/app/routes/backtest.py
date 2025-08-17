"""Backtesting endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from app.services import ml_service

router = APIRouter(prefix="/backtest", tags=["backtest"])


@router.get("/{symbol}")
def run_backtest(symbol: str):
    """Run a small backtest using the internal ML service."""

    return ml_service.backtest(symbol)

