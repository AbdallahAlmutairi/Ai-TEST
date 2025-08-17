"""Security related helper functions."""

from __future__ import annotations

import secrets
from typing import Any

from werkzeug.security import check_password_hash, generate_password_hash


def hash_password(password: str) -> str:
    """Hash a password using Werkzeug's secure helper."""

    return generate_password_hash(password)


def verify_password(password: str, hashed: str) -> bool:
    """Verify a password against an existing hash."""

    return check_password_hash(hashed, password)


def generate_token(length: int = 24) -> str:
    """Return a random hexadecimal token."""

    return secrets.token_hex(length)


__all__ = ["hash_password", "verify_password", "generate_token"]

