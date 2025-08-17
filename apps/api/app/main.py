"""Entry point for the FastAPI application."""

from fastapi import FastAPI

from app.db.seed import init_db
from app.routes import auth, backtest, news, recs
from app.ws import stream

app = FastAPI(title="AI Project API")

app.include_router(auth.router)
app.include_router(backtest.router)
app.include_router(news.router)
app.include_router(recs.router)
app.include_router(stream.router)

# Ensure the database exists even if startup events are not triggered
init_db()


@app.on_event("startup")
def _startup() -> None:
    """Initialize database tables on startup."""
    init_db()
