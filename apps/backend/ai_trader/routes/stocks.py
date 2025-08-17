from flask import Blueprint, request
from ai_trader.services.data_providers.yfinance_client import get_quote, get_history
from ai_trader.services.indicators import compute_indicators

bp = Blueprint('stocks', __name__, url_prefix='/api/stocks')


@bp.get('/quote')
def quote():
    symbol = request.args.get('symbol', '').upper()
    data = get_quote(symbol)
    return data or {'error': 'symbol not found'}, (200 if data else 404)


@bp.get('/history')
def history():
    symbol = request.args.get('symbol', '').upper()
    range_ = request.args.get('range', '1mo')
    interval = request.args.get('interval', '1d')
    data = get_history(symbol, range_, interval)
    return data or {'error': 'symbol not found'}, (200 if data else 404)


@bp.get('/indicators')
def indicators():
    symbol = request.args.get('symbol', '').upper()
    range_ = request.args.get('range', '1mo')
    interval = request.args.get('interval', '1d')
    hist = get_history(symbol, range_, interval)
    if not hist:
        return {'error': 'symbol not found'}, 404
    ind = compute_indicators(hist)
    return ind
