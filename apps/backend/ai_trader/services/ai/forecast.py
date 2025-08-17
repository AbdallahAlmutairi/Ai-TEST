from .model_registry import load_model


def predict(symbol: str):
    model = load_model()
    # Placeholder: random prediction
    return {
        'symbol': symbol,
        'direction': 'sideways',
        'target': None,
        'confidence': 0.0,
        'rationale': ['Model not trained']
    }
