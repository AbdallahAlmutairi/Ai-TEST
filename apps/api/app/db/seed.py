"""Utilities for seeding the database with initial data."""

from app.db.session import SessionLocal, engine
from app.models import orm


def init_db() -> None:
    """Create tables and insert a few sample recommendations."""
    orm.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if not db.query(orm.Recommendation).first():
            db.add_all(
                [
                    orm.Recommendation(ticker="AAPL", rating="buy"),
                    orm.Recommendation(ticker="MSFT", rating="hold"),
                ]
            )
            db.commit()
    finally:
        db.close()
