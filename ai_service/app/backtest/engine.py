"""Very small backtesting engine for demonstration."""
from __future__ import annotations

from datetime import date
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd

from ..data.csv_source import CSVSource
from ..features import featurizer
from ..signals.generator import prob_to_action
from ..models.model_store import load_model


def run_backtest(symbol: str, start: date | None = None, end: date | None = None, interval: str = "1d") -> Tuple[Dict[str, float], List[Dict[str, float]], List[Dict[str, float]]]:
    source = CSVSource()
    df = source.get_ohlcv(symbol, start=start, end=end, interval=interval)
    features, _ = featurizer.build_matrix(df)
    bundle = load_model()
    model = bundle["model"]
    scaler = bundle["scaler"]
    X = scaler.transform(features)
    probs = model.predict_proba(X)[:, 1]
    actions = [prob_to_action(p) for p in probs]
    df = df.iloc[-len(actions):]
    df["return"] = df["Close"].pct_change().fillna(0)
    position = 0
    positions = []
    for act in actions:
        if act == "Buy":
            position = 1
        elif act == "Sell":
            position = 0
        positions.append(position)
    strat_returns = df["return"].values * np.array([0] + positions[:-1])
    equity = (1 + strat_returns).cumprod()
    equity_series = pd.Series(equity, index=features.index)
    max_dd = (equity_series.cummax() - equity_series).max()
    cagr = equity_series.iloc[-1] ** (252 / len(equity_series)) - 1
    sharpe = strat_returns.mean() / (strat_returns.std() + 1e-8) * np.sqrt(252)
    win_rate = (strat_returns > 0).mean()
    metrics = {
        "CAGR": float(cagr),
        "MaxDD": float(max_dd),
        "Sharpe": float(sharpe),
        "WinRate": float(win_rate),
    }
    equity_curve = [{"t": idx.isoformat(), "v": float(val)} for idx, val in equity_series.items()]
    return metrics, equity_curve, []
