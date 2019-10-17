import os

application_name = 'plates'
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    FLASK_APP = application_name
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dbuser:dbpassword@localhost/plates'
    SQLALCHEMY_POOL_TIMEOUT = 600
    SQLALCHEMY_POOL_RECYCLE = 300
    SQLALCHEMY_POOL_PRE_PING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '425BF6E9E8BB1CCCAD5845EFE599B'
