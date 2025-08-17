"""Data source interface for fetching market data."""
from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date
from typing import Optional

import pandas as pd


class IDataSource(ABC):
    """Abstract data source providing OHLCV data."""

    @abstractmethod
    def get_ohlcv(
        self,
        symbol: str,
        start: Optional[date] = None,
        end: Optional[date] = None,
        interval: str = "1d",
    ) -> pd.DataFrame:
        """Return OHLCV data for the given symbol and date range."""

