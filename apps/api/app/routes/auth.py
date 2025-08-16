"""Authentication routes."""

from fastapi import APIRouter

from app.core import security

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
def login(username: str, password: str):
    """Return a fake access token for demonstration purposes."""
    token = security.hash_password(password)
    return {"access_token": token, "token_type": "bearer"}
