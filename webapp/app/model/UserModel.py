from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.dao import daoPool
db = daoPool.sqlDAO

from app import app



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), nullable=False, comment='Логин', unique=True)
    password = db.Column(db.String(120), nullable=False, comment='Пароль')
    name = db.Column(db.String(120), comment='Имя пользователя')

    def generate_auth_token(self, expiration=80000):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        data = s.loads(token)
        return User.query.get(data['id'])

    def __init__(self, login, password):
            self.login = login
            self.password = password

    def __repr__(self):
        return '<User %r>' % self.login



