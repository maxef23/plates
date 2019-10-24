from flask_sqlalchemy import SQLAlchemy
from app.model import init_model
from app.dao.esDAO import ElasticsearchDAO

class DaoPool():

    sqlDAO = None
    esDAO = None
    def __init__(self):
        pass

    def init_app(self, app):
        # db init

        self.sqlDAO = SQLAlchemy(app)
        init_model(self.sqlDAO)

        self.esDAO = ElasticsearchDAO('http://localhost', \
                                        '9200')

daoPool = DaoPool()