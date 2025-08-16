"""Minimal security helpers."""

from hashlib import sha256


def hash_password(password: str) -> str:
    """Return a SHA256 hash of the provided password."""
    return sha256(password.encode("utf-8")).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against a given hash."""
    return hash_password(password) == hashed
