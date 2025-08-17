from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@bp.post('/register')
def register():
    return {'message': 'register'}, 501


@bp.post('/login')
def login():
    return {'message': 'login'}, 501
