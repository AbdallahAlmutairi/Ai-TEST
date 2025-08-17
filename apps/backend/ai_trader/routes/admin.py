from flask import Blueprint

bp = Blueprint('admin', __name__, url_prefix='/api/admin')


@bp.get('/errors')
def errors():
    return {'errors': []}


@bp.get('/metrics')
def metrics():
    return {'metrics': {}}
