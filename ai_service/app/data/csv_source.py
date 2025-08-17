"""CSV data source for demo purposes."""
from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

from .source_base import IDataSource

BASE_PATH = Path(__file__).resolve().parents[2] / "data_samples"


class CSVSource(IDataSource):
    """Load OHLCV data from CSV files in ``data_samples`` directory.

    When the requested CSV file is not found, a deterministic synthetic data
    set is generated so that the demo and tests can run without any external
    data files.
    """

    def __init__(self, base_path: Path = BASE_PATH):
        self.base_path = base_path

    def _resolve_path(self, symbol: str) -> Path:
        sym = symbol.replace(".", "_")
        if not sym.startswith("TASI_"):
            sym = f"TASI_{sym.split('_')[0]}"
        return self.base_path / f"{sym}.csv"

    def _synthetic(self, start: Optional[date], end: Optional[date]) -> pd.DataFrame:
        """Generate a simple synthetic OHLCV data set."""
        end_date = pd.to_datetime(end or date.today())
        rng = pd.date_range(end=end_date, periods=250, freq="D")
        rs = np.random.RandomState(0)
        price = 100 + rs.randn(len(rng)).cumsum()
        df = pd.DataFrame(
            {
                "Open": price,
                "High": price + rs.rand(len(rng)),
                "Low": price - rs.rand(len(rng)),
                "Close": price,
                "Volume": rs.randint(1000, 5000, len(rng)),
            },
            index=rng,
        )
        if start:
            df = df[df.index >= pd.to_datetime(start)]
        if end:
            df = df[df.index <= pd.to_datetime(end)]
        return df

    def get_ohlcv(
        self,
        symbol: str,
        start: Optional[date] = None,
        end: Optional[date] = None,
        interval: str = "1d",
    ) -> pd.DataFrame:
        path = self._resolve_path(symbol)
        try:
            df = pd.read_csv(path, parse_dates=["Date"]).set_index("Date")
        except FileNotFoundError:
            df = self._synthetic(start, end)
        else:
            if start:
                df = df[df.index >= pd.to_datetime(start)]
            if end:
                df = df[df.index <= pd.to_datetime(end)]
        return df
