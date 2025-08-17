from flask import Flask

from ai_trader.routes import register_blueprints


def create_app() -> Flask:
    """Application factory."""
    app = Flask(__name__)
    register_blueprints(app)

    @app.route('/api/health')
    def health() -> dict:
        return {"ok": True, "version": "0.1.0"}

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
