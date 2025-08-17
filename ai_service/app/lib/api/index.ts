export interface AnalyzeOptions { interval?: string; locale?: 'en' | 'ar'; }
export interface AnalyzeResponse {
  symbol: string;
  price: number;
  action: string;
  confidence: number;
  horizon: string;
  reasons: string[];
  indicators: Record<string, number>;
  timestamp: string;
  disclaimer: string;
}

const BASE = '';

export async function analyzeSymbol(symbol: string, opts: AnalyzeOptions = {}): Promise<AnalyzeResponse> {
  const body = { symbol, interval: opts.interval ?? '1d', locale: opts.locale ?? 'en' };
  const res = await fetch(`${BASE}/ai/analyze`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body)
  });
  if (!res.ok) throw new Error('request failed');
  return res.json();
}

export async function getSignals(symbols: string[]): Promise<any> {
  const res = await fetch(`${BASE}/ai/signals`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ symbols, interval: '1d' })
  });
  return res.json();
}

export async function runBacktest(params: any): Promise<any> {
  const res = await fetch(`${BASE}/ai/backtest`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(params)
  });
  return res.json();
}
