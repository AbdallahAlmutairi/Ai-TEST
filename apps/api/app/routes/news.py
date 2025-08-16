"""News endpoints."""

from fastapi import APIRouter

router = APIRouter(prefix="/news", tags=["news"])


@router.get("/")
def latest_news():
    """Return a list of sample news articles."""
    return [{"headline": "Market opens higher"}]
