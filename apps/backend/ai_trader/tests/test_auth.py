from apps.backend.app import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    res = client.get('/api/health')
    assert res.status_code == 200
