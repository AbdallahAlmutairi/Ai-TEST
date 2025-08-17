from flask import Blueprint

bp = Blueprint('alerts', __name__, url_prefix='/api/alerts')


@bp.post('')
def create():
    return {'message': 'create alert'}, 501


@bp.get('')
def list_alerts():
    return {'alerts': []}
