"""Computation of technical indicators."""
from __future__ import annotations

import pandas as pd
import numpy as np


def sma(series: pd.Series, window: int) -> pd.Series:
    return series.rolling(window=window).mean()


def ema(series: pd.Series, window: int) -> pd.Series:
    return series.ewm(span=window, adjust=False).mean()


def rsi(series: pd.Series, window: int = 14) -> pd.Series:
    delta = series.diff()
    gain = pd.Series(np.where(delta > 0, delta, 0.0), index=series.index)
    loss = pd.Series(np.where(delta < 0, -delta, 0.0), index=series.index)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


def macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9) -> pd.DataFrame:
    ema_fast = ema(series, fast)
    ema_slow = ema(series, slow)
    macd_line = ema_fast - ema_slow
    signal_line = ema(macd_line, signal)
    return pd.DataFrame({"macd": macd_line, "macd_signal": signal_line})


def bollinger_pband(series: pd.Series, window: int = 20, ndev: float = 2.0) -> pd.Series:
    sma_ = sma(series, window)
    std = series.rolling(window).std()
    upper = sma_ + ndev * std
    lower = sma_ - ndev * std
    return (series - lower) / (upper - lower)


def atr(high: pd.Series, low: pd.Series, close: pd.Series, window: int = 14) -> pd.Series:
    high_low = high - low
    high_close = (high - close.shift()).abs()
    low_close = (low - close.shift()).abs()
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    return true_range.rolling(window).mean()
