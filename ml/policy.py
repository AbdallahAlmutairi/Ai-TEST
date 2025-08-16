"""Simple policy utilities."""


def apply_policy(prediction: str, risk: str) -> str:
    """Combine a model prediction with a risk profile."""
    return f"{prediction}-{risk}"
