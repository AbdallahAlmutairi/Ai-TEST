from datetime import datetime
from ai_trader.extensions import db


class NewsItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(20))
    headline = db.Column(db.Text)
    sentiment = db.Column(db.Float)
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
