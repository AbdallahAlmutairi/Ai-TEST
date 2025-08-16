"""Toy training pipeline."""

from .features import compute_moving_average
from .model import predict


def train_model(data: list[float]) -> str:
    """Train the model on data and return a prediction."""
    feature = compute_moving_average(data)
    return predict(feature)
