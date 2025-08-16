"""Backtest endpoints."""

from fastapi import APIRouter

router = APIRouter(prefix="/backtest", tags=["backtest"])


@router.get("/")
def run_backtest():
    """Return a placeholder backtest result."""
    return {"result": "success"}
