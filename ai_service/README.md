# AI Trading Consultant Service

This is a small demonstration FastAPI service that analyses market data and
produces simple trading signals.  It includes a minimal training pipeline and
unit tests.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn ai_service.app.main:app --reload --port 8001
```

By default the service uses synthetic data and a tiny built-in model. To train
your own model on real OHLCV data:

```bash
python -m ai_service.app.models.trainer --symbol 1010.SR --data path/to/your.csv --out ai_service/app/models/model.joblib
```

## API

- `GET /health` – basic health check
- `POST /ai/analyze` – analyse a symbol and return an action with reasons

Example:

```bash
curl -X POST http://localhost:8001/ai/analyze -H 'Content-Type: application/json' \\
  -d '{"symbol": "1010.SR", "interval": "1d"}'
```
