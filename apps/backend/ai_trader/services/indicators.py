import pandas as pd
import ta


def compute_indicators(history: list[dict]):
    df = pd.DataFrame(history)
    if 'Close' not in df.columns:
        return {}
    df.set_index('Date', inplace=True)
    result = {
        'rsi': ta.momentum.rsi(df['Close']).iloc[-1],
        'macd': ta.trend.macd_diff(df['Close']).iloc[-1],
        'sma': ta.trend.sma_indicator(df['Close']).iloc[-1],
        'ema': ta.trend.ema_indicator(df['Close']).iloc[-1],
        'bb_high': ta.volatility.bollinger_hband(df['Close']).iloc[-1],
        'bb_low': ta.volatility.bollinger_lband(df['Close']).iloc[-1],
    }
    return {k: float(v) for k, v in result.items() if pd.notna(v)}
