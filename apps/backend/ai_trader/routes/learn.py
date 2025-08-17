from flask import Blueprint

bp = Blueprint('learn', __name__, url_prefix='/api/learn')


@bp.get('/lessons')
def lessons():
    return {'lessons': []}


@bp.get('/quizzes')
def quizzes():
    return {'quizzes': []}
