import pathlib, sys
sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from ai_service.app.models import infer


def test_analyze_basic():
    res = infer.analyze("1010.SR")
    assert res["action"] in {"Buy", "Sell", "Hold"}
    assert 0 <= res["confidence"] <= 1
    assert len(res["reasons"]) >= 3
    assert "disclaimer" in res
