"""Simple training pipeline for logistic regression model."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from ..features import featurizer
from .model_store import save_model


def train(symbol: str, data_path: Path, out_path: Path) -> None:
    df = pd.read_csv(data_path, parse_dates=["Date"])
    features, target = featurizer.build_matrix(df)
    scaler = StandardScaler()
    X = scaler.fit_transform(features)
    X_train, X_test, y_train, y_test = train_test_split(X, target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"Model accuracy: {acc:.3f}")
    save_model(model, scaler, out_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Train logistic regression model")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    train(args.symbol, Path(args.data), Path(args.out))


if __name__ == "__main__":  # pragma: no cover
    main()
