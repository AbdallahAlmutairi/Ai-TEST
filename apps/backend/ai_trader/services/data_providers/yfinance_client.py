import yfinance as yf


"""Lightweight wrappers around the ``yfinance`` package."""

try:  # pragma: no cover - dependency may be missing in tests
    import yfinance as yf  # type: ignore
except Exception:  # pragma: no cover - executed when package is missing
    yf = None  # type: ignore


def get_quote(symbol: str):
    if not symbol or yf is None:
        return None
    ticker = yf.Ticker(symbol)
    info = getattr(ticker, "info", {})
    if not info:
        return None
    return {"symbol": symbol, "price": info.get("regularMarketPrice")}


def get_history(symbol: str, range_: str, interval: str):
    if not symbol or yf is None:
        return None
    try:
        hist = yf.download(symbol, period=range_, interval=interval, progress=False)
    except Exception:
        return None
    if hist.empty:
        return None
    hist.reset_index(inplace=True)
    return hist.to_dict(orient="records")
