"""Application configuration for the API."""

from pydantic import BaseModel


class Settings(BaseModel):
    """Simple settings object used by the application."""

    database_url: str = "sqlite:///./test.db"
    secret_key: str = "change-me"
    token_algorithm: str = "HS256"


settings = Settings()
