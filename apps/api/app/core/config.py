"""Application configuration using Pydantic settings."""

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Simple settings object used by the application."""

    database_url: str = "sqlite:///./test.db"
    secret_key: str = "change-me"
    token_algorithm: str = "HS256"


settings = Settings()
