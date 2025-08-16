"""Routes related to investment recommendations."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import orm, schemas

router = APIRouter(prefix="/recs", tags=["recs"])


@router.get("/", response_model=list[schemas.Recommendation])
def list_recommendations(db: Session = Depends(get_db)):
    """Return all recommendations from the database."""
    return db.query(orm.Recommendation).all()
