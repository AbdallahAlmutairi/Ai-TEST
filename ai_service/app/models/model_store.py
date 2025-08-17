"""Model persistence utilities."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import joblib
import numpy as np

from ..config import get_settings

settings = get_settings()
MODEL_PATH = Path(settings.MODEL_PATH)
MODEL_VERSION = "0.1.0"


def save_model(model: Any, scaler: Any, path: Path = MODEL_PATH) -> None:
    """Persist model and scaler to disk."""
    data = {
        "model": model,
        "scaler": scaler,
        "version": MODEL_VERSION,
        "timestamp": datetime.utcnow(),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(data, path)


class _DummyModel:
    """Fallback model returning neutral probabilities."""

    def predict_proba(self, X: np.ndarray) -> np.ndarray:  # pragma: no cover - trivial
        return np.tile([0.5, 0.5], (X.shape[0], 1))


class _DummyScaler:
    """Identity transformer used when no scaler is available."""

    def transform(self, X: np.ndarray) -> np.ndarray:  # pragma: no cover - trivial
        return X


def load_model(path: Path = MODEL_PATH) -> Dict[str, Any]:
    """Load model and scaler from disk.

    If the model file is missing, a simple fallback model and scaler are
    provided so that the service can operate without any binary assets.
    """

    try:
        return joblib.load(path)
    except FileNotFoundError:
        return {
            "model": _DummyModel(),
            "scaler": _DummyScaler(),
            "version": MODEL_VERSION,
            "timestamp": datetime.utcnow(),
        }
