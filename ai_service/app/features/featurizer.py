"""Utilities to assemble a feature matrix from raw OHLCV data."""
from __future__ import annotations

import pandas as pd

from . import indicators


FEATURE_COLUMNS = [
    "rsi",
    "macd",
    "macd_signal",
    "bollinger_b",
    "atr",
    "returns",
    "volatility",
]


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    close = df["Close"]
    df["sma_20"] = indicators.sma(close, 20)
    df["ema_20"] = indicators.ema(close, 20)
    df["rsi"] = indicators.rsi(close, 14)
    macd_df = indicators.macd(close)
    df = df.join(macd_df)
    df["bollinger_b"] = indicators.bollinger_pband(close)
    df["atr"] = indicators.atr(df["High"], df["Low"], close)
    df["returns"] = close.pct_change()
    df["volatility"] = df["returns"].rolling(20).std()
    df["target"] = (close.shift(-1) > close).astype(int)
    return df


def build_matrix(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    df = add_features(df)
    df = df.dropna()
    features = df[FEATURE_COLUMNS]
    target = df["target"]
    return features, target
