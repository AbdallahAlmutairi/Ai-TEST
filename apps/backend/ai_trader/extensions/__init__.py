"""Application extensions used across the backend service.

Each extension is instantiated in its own module (``cache``, ``db``,
``jwt`` and ``limiter``).  This lightweight module simply exposes them and
provides a helper :func:`init_app` that wires everything to a Flask
application instance.
"""

from flask_cors import CORS

from .cache import cache
from .db import db
from .jwt import jwt
from .limiter import limiter


def init_app(app) -> None:
    """Initialise all extensions with the provided Flask app.

    Parameters
    ----------
    app: :class:`flask.Flask`
        The application instance to configure.
    """

    # Enable CORS for all routes – this keeps the example simple.
    CORS(app)

    # Initialise database, JWT, caching and rate limiting extensions.
    db.init_app(app)
    jwt.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)


__all__ = ["cache", "db", "jwt", "limiter", "init_app"]

