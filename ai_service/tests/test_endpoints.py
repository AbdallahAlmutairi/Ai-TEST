import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from ai_service.app.main import health, ai_analyze, AnalyzeRequest


def test_health_function():
    res = health()
    assert res["status"] == "ok"


def test_analyze_via_route_function():
    req = AnalyzeRequest(symbol="1010.SR", interval="1d")
    res = ai_analyze(req)
    assert res.symbol == "1010.SR"
    assert res.action in {"Buy", "Sell", "Hold"}
    assert len(res.reasons) >= 3
