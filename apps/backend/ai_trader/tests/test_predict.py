from apps.backend.app import create_app


def test_predict_endpoint():
    app = create_app()
    client = app.test_client()
    res = client.post('/api/predict', json={'symbol': 'AAPL'})
    assert res.status_code == 200
    data = res.get_json()
    assert 'direction' in data
