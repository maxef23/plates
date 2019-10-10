import logging
import os
from flask import Flask
from flask_cors import CORS, cross_origin

from flask import jsonify
from flask import request

CONFIG_NAME_MAPPER = {
    'development': 'config.Development.cfg',
    'testing': 'config.Testing.cfg',
    'production': 'config.Production.cfg'
}

def create_app(flask_config_name=None):
    '''' create flask app '''

    ## Load Config
    env_flask_config_name = os.getenv('FLASK_CONFIG')
    if not env_flask_config_name and flask_config_name is None:
        flask_config_name = 'development'
    elif flask_config_name is None:
        flask_config_name = env_flask_config_name


    try:
        if CONFIG_NAME_MAPPER[flask_config_name] is None:
            return None
    except KeyError:
        return None

    ## Creat app
    app = Flask(__name__)
    app.config.from_pyfile(CONFIG_NAME_MAPPER[flask_config_name])
    app.config.SWAGGER_UI_JSONEDITOR = True
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

    # db init
    from app.dao import daoPool
    daoPool.init_app(app)

    from app.model.NumberplateModel import Numberplate

    @app.route('/get', methods=['GET'])
    def get():
        list = []
        plates = Numberplate.query.all()
        for plate in plates:
            list.append({'id' : plate.id, 'CamID' : plate.CamID, 'Timestamp' : plate.Timestamp, 'Licplates' : plate.Licplates})
        return jsonify(list)



    @app.route('/get/<int:id>', methods=['GET'])
    def get_by_id(id):
        list = []
        plates = Numberplate.query.filter(Numberplate.id>=id)
        for plate in plates:
            list.append({'id' : plate.id, 'CamID' : plate.CamID, 'Timestamp' : plate.Timestamp, 'Licplates' : plate.Licplates})
        return jsonify(list)
        


    @app.route('/send', methods=['POST'])
    def send(CamID = None, Timestamp = None, Licplates = None):
        if (request):
            plate = Numberplate(request.form['CamID'], request.form['Timestamp'], request.form['Licplates'])
        elif (CamID is not None and Timestamp is not None and Licplates is not None):
            plate = Numberplate(CamID, Timestamp, Licplates)
        else:
            return '';
        daoPool.sqlDAO.session.add(plate)
        daoPool.sqlDAO.session.commit()
        return 'Send'


    return app


