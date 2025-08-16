"""Script to initialise the local database with mock data."""

from apps.api.app.db.seed import init_db


if __name__ == "__main__":
    init_db()
