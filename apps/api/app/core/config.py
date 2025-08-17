# apps/api/app/core/config.py
"""
Application configuration (merged resolution).
Use environment variables; no external dependencies.
"""

import os
from dataclasses import dataclass

def _getenv(name: str, default: str) -> str:
    val = os.getenv(name)
    return val if val not in (None, "") else default

@dataclass
class Settings:
    # DB & Security
    database_url: str = _getenv("DATABASE_URL", "sqlite:///./test.db")
    secret_key: str = _getenv("JWT_SECRET_KEY", "change-me")
    token_algorithm: str = _getenv("TOKEN_ALGORITHM", "HS256")

    # Optional flags
    debug: bool = _getenv("DEBUG", "false").lower() == "true"

settings = Settings()
