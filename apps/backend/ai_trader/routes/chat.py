from flask import Blueprint, request

bp = Blueprint('chat', __name__, url_prefix='/api')


@bp.post('/chat')
def chat():
    data = request.get_json(force=True)
    message = data.get('message', '')
    return {'reply': f'You said: {message}', 'references': []}
