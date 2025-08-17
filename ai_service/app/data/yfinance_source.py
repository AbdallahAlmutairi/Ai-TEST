"""Yahoo Finance data source (optional)."""
from __future__ import annotations

from datetime import date
from typing import Optional

import pandas as pd

try:
    import yfinance as yf
except Exception:  # pragma: no cover - yfinance may not be installed
    yf = None

from .source_base import IDataSource


class YFinanceSource(IDataSource):
    """Fetch OHLCV data using the :mod:`yfinance` package."""

    def get_ohlcv(
        self,
        symbol: str,
        start: Optional[date] = None,
        end: Optional[date] = None,
        interval: str = "1d",
    ) -> pd.DataFrame:
        if yf is None:  # pragma: no cover - simple guard
            raise RuntimeError("yfinance not available")
        data = yf.download(symbol, start=start, end=end, interval=interval)
        data.index.name = "Date"
        return data
