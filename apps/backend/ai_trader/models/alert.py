from datetime import datetime
from ai_trader.extensions import db


class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    condition = db.Column(db.String(50))
    value = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
