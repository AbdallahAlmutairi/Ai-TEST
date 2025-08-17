from flask import Blueprint

bp = Blueprint('payments', __name__, url_prefix='/api/payments')


@bp.post('/webhook')
def webhook():
    return {'received': True}
