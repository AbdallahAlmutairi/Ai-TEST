import yfinance as yf


def get_quote(symbol: str):
    if not symbol:
        return None
    ticker = yf.Ticker(symbol)
    info = ticker.info
    if not info:
        return None
    return {
        'symbol': symbol,
        'price': info.get('regularMarketPrice')
    }


def get_history(symbol: str, range_: str, interval: str):
    if not symbol:
        return None
    try:
        hist = yf.download(symbol, period=range_, interval=interval, progress=False)
    except Exception:
        return None
    if hist.empty:
        return None
    hist.reset_index(inplace=True)
    return hist.to_dict(orient='records')
