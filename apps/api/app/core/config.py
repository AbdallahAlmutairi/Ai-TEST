"""Minimal application settings without external dependencies."""

from dataclasses import dataclass


@dataclass
class Settings:
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "change-me"
    token_algorithm: str = "HS256"


settings = Settings()

