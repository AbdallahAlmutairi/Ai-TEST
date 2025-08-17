"""FastAPI application entrypoint."""
from __future__ import annotations

import pandas as pd
from fastapi import FastAPI

from .config import get_settings
from .models import infer
from .backtest.engine import run_backtest
from .schemas import (
    AnalyzeRequest,
    AnalyzeResponse,
    BacktestRequest,
    BacktestResponse,
    ChatRequest,
    ChatResponse,
    ExplainRequest,
    ExplainResponse,
    Signal,
    SignalsRequest,
    SignalsResponse,
)
from .signals.explain import build_reasons
from .models.model_store import MODEL_VERSION

app = FastAPI(title="AI Trading Consultant")
settings = get_settings()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "version": "0.1.0", "model_version": MODEL_VERSION}


@app.post("/ai/analyze", response_model=AnalyzeResponse)
def ai_analyze(req: AnalyzeRequest) -> AnalyzeResponse:
    return AnalyzeResponse(**infer.analyze(req.symbol, req.start, req.end, req.interval, req.locale))


@app.post("/ai/signals", response_model=SignalsResponse)
def ai_signals(req: SignalsRequest) -> SignalsResponse:
    base_disclaimer = (
        "For research and education only. Not financial advice."
        if req.locale != "ar"
        else "لأغراض البحث والتعليم فقط. ليست نصيحة استثمارية."
    )
    signals: list[Signal] = []
    last_res = None
    for sym in req.symbols:
        res = infer.analyze(sym, interval=req.interval, locale=req.locale)
        if req.minConfidence is not None and res["confidence"] < req.minConfidence:
            continue
        signals.append(
            Signal(
                symbol=sym,
                action=res["action"],
                confidence=res["confidence"],
                reasons=res["reasons"],
                updatedAt=res["timestamp"],
            )
        )
        last_res = res
    disclaimer = last_res["disclaimer"] if signals else base_disclaimer
    return SignalsResponse(signals=signals, disclaimer=disclaimer)


@app.post("/ai/backtest", response_model=BacktestResponse)
def ai_backtest(req: BacktestRequest) -> BacktestResponse:
    metrics, equity, trades = run_backtest(req.symbol, req.start, req.end, req.interval)
    disclaimer = "For research and education only. Not financial advice."
    return BacktestResponse(metrics=metrics, equity=equity, trades=trades, disclaimer=disclaimer)


@app.post("/ai/explain", response_model=ExplainResponse)
def ai_explain(req: ExplainRequest) -> ExplainResponse:
    res = infer.analyze(req.symbol, locale=req.locale)
    indicators = res["indicators"]
    top_features = [
        {"name": k, "weight": float(v), "direction": 1 if v >= 0 else -1}
        for k, v in list(indicators.items())[:3]
    ]
    narrative = ", ".join(build_reasons(pd.Series({"Close": res["price"]}), pd.Series(indicators), req.locale))
    return ExplainResponse(topFeatures=top_features, narrative=narrative, disclaimer=res["disclaimer"])


@app.post("/ai/chat", response_model=ChatResponse)
def ai_chat(req: ChatRequest) -> ChatResponse:
    msg = req.message.lower()
    if "risk" in msg:
        reply = "Investing involves risk." if req.locale == "en" else "الاستثمار ينطوي على مخاطر."
    elif "signal" in msg:
        reply = "Use /ai/analyze to get signals." if req.locale == "en" else "استخدم /ai/analyze للحصول على الإشارات."
    else:
        reply = "Hello" if req.locale == "en" else "مرحبا"
    disclaimer = "For research and education only. Not financial advice." if req.locale != "ar" else "لأغراض البحث والتعليم فقط. ليست نصيحة استثمارية."
    return ChatResponse(reply=reply, disclaimer=disclaimer)
