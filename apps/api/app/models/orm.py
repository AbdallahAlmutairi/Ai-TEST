"""SQLAlchemy ORM models."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Recommendation(Base):
    """Simple recommendation model."""

    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    rating = Column(String, nullable=False)
