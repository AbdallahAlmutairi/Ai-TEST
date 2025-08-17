"""Flask application factory for the backend service."""

from flask import Flask

from .ai_trader.routes import register_blueprints
from .ai_trader.extensions import init_app as init_extensions


def create_app() -> Flask:
    """Application factory."""
    app = Flask(__name__)
    # Basic configuration for demo purposes
    app.config.setdefault("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    # Initialise shared extensions (database, caching, rate limiting, ...)
    init_extensions(app)
    # Register API blueprints
    register_blueprints(app)

    @app.route('/api/health')
    def health() -> dict:
        return {"ok": True, "version": "0.1.0"}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
