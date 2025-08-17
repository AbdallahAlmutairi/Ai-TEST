"""Simplified application configuration without external dependencies."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class Settings:
    DATA_SOURCE: str = os.getenv("DATA_SOURCE", "csv")
    CACHE_URL: str = os.getenv("CACHE_URL", "redis://localhost:6379/0")
    MODEL_PATH: str = os.getenv("MODEL_PATH", "ai_service/app/models/model.joblib")
    DEFAULT_INTERVAL: str = os.getenv("DEFAULT_INTERVAL", "1d")


def get_settings() -> Settings:
    return Settings()
