"""Pydantic models used by the API."""

from pydantic import BaseModel


class Recommendation(BaseModel):
    id: int
    ticker: str
    rating: str

    class Config:
        orm_mode = True
