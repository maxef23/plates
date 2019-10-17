#!flask/bin/python
import os
from flask import Flask

from flask_cors import CORS, cross_origin

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from preferences import Config
from preferences import application_name

app = Flask(application_name)
app.config.from_object(Config)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# db init
from app.dao import daoPool
daoPool.init_app(app)
db = daoPool.sqlDAO
migrate = Migrate(app, db)


from app import api




