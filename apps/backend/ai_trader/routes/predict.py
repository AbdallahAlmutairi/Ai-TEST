from flask import Blueprint, request
from ai_trader.services.ai.forecast import predict

bp = Blueprint('predict', __name__, url_prefix='/api')


@bp.post('/predict')
def do_predict():
    data = request.get_json(force=True)
    symbol = data.get('symbol', '')
    return predict(symbol)
