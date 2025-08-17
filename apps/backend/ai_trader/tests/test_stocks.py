from apps.backend.app import create_app

def test_quote_missing_symbol():
    app = create_app()
    client = app.test_client()
    res = client.get('/api/stocks/quote')
    assert res.status_code == 404
