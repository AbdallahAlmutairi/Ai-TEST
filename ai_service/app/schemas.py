"""Pydantic models for request and response bodies."""
from __future__ import annotations

from datetime import date, datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    symbol: str
    start: Optional[date] = None
    end: Optional[date] = None
    interval: str = Field(default="1d")
    locale: str = Field(default="en", pattern="^(en|ar)$")


class AnalyzeResponse(BaseModel):
    symbol: str
    price: float
    action: str
    confidence: float
    horizon: str
    reasons: List[str]
    indicators: Dict[str, float]
    timestamp: datetime
    disclaimer: str


class SignalsRequest(BaseModel):
    symbols: List[str]
    interval: str = "1d"
    minConfidence: float | None = None
    locale: str = "en"


class Signal(BaseModel):
    symbol: str
    action: str
    confidence: float
    reasons: List[str]
    updatedAt: datetime


class SignalsResponse(BaseModel):
    signals: List[Signal]
    disclaimer: str


class BacktestRequest(BaseModel):
    symbol: str
    start: date | None = None
    end: date | None = None
    interval: str = "1d"


class Trade(BaseModel):
    entry: datetime
    exit: datetime
    pnl: float


class BacktestResponse(BaseModel):
    metrics: Dict[str, float]
    equity: List[Dict[str, float]]
    trades: List[Trade]
    disclaimer: str


class ExplainRequest(BaseModel):
    symbol: str
    asOf: Optional[date] = None
    locale: str = "en"


class FeatureWeight(BaseModel):
    name: str
    weight: float
    direction: int


class ExplainResponse(BaseModel):
    topFeatures: List[FeatureWeight]
    narrative: str
    disclaimer: str


class ChatRequest(BaseModel):
    message: str
    context: Optional[Dict[str, str]] = None
    locale: str = "en"


class ChatResponse(BaseModel):
    reply: str
    disclaimer: str
