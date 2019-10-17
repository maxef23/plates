from functools import wraps
from itsdangerous import BadSignature, SignatureExpired, TimedJSONWebSignatureSerializer as Serializer
from sqlalchemy.exc import IntegrityError, InvalidRequestError

from flask import Response, request

from app.model.UserModel import User


class BadRequest(Exception):

    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        result = dict(self.payload or ())
        result['message'] = self.message
        return result


def get_user_id_by_token(token):
    if not token:
        return None
    try:
        s = Serializer(app.config['SECRET_KEY'])
        data = s.loads(token)
        return data['id']
    except:
        return None


def get_user_by_token(token):
    s = Serializer(app.config['SECRET_KEY'], expires_in=1200)
    if token is None:
        raise BadRequest(message='Вы не зашли в систему', status_code=401)
    try:
        data = s.loads(token)
        user_id = data['id']
        user = User.query.filter_by(id=user_id)
        if user is None:
            raise BadRequest(message='Не найден пользователь [id={}]'.format(user_id), status_code=401)
        return user
    except SignatureExpired:
        raise BadRequest(message='Сессия закончена. Перезайдите', status_code=401)
    except BadSignature:
        raise BadRequest(message='Неверный ключ сессии. Перезайдите', status_code=401)
    except InvalidRequestError:
        return get_user_by_token(token)


def login_required(func):
    @wraps(func)
    def wrapper():
        try:
            token = request.args.get('token', None)
            user = get_user_by_token(token)
            return func(user)
        except BadRequest as e:
            return Response(e.message, status=e.status_code)

    return wrapper


