"""JWT authentication extension instance."""

from flask_jwt_extended import JWTManager

jwt = JWTManager()

__all__ = ["jwt"]

