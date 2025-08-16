"""Very small placeholder predictive model."""


def predict(feature: float) -> str:
    """Return a naive prediction based on feature sign."""
    return "buy" if feature >= 0 else "sell"
