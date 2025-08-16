"""Database session and engine setup."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.database_url, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    """Yield a database session for request handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
