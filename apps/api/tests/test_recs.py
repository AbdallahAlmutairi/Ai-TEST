"""Tests for the recommendations endpoint."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_recommendations():
    """The API should return the seeded recommendations."""
    response = client.get("/recs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) and data
    assert data[0]["ticker"] == "AAPL"
