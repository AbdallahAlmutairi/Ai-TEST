"""Rate limiting extension instance."""

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Basic IP based limiter used for demonstration purposes.
limiter = Limiter(key_func=get_remote_address)

__all__ = ["limiter"]

