from app import app, db
from app import utils

from flask import jsonify
from flask import Response, request

import datetime
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

from app.model.NumberplateModel import Numberplate
from app.model.UserModel import User


def create_json(array):
    list = []
    for item in array:
        list.append({'id' : item.id, 'CamID' : item.CamID, 'Timestamp' : item.Timestamp, 'Licplates' : item.Licplates})
    return jsonify(list)

@app.route('/login', methods=['POST'])
def login():
    in_login = request.form['login']
    in_password = request.form['password']
    current_user = User.query.filter_by(login=in_login).first()
    if current_user is None or not current_user.password == in_password:
        return Response('Логин или пароль не верны', status=406)
    else:
        return jsonify({'token': current_user.generate_auth_token().decode('utf-8')})

@app.route('/get', methods=['GET'])
@login_required
def get():
    return create_json(Numberplate.query.all())

@app.route('/send', methods=['POST'])
@login_required
def send(CamID = None, Timestamp = None, Licplates = None):
    if (Timestamp or request.form['Timestamp']):
        time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    if (request):
        plate = Numberplate(request.form['CamID'], time, request.form['Licplates'])
    elif (CamID is not None and Timestamp is not None and Licplates is not None):
        plate = Numberplate(CamID, time, Licplates)
    else:
        return '';
    daoPool.sqlDAO.session.add(plate)
    daoPool.sqlDAO.session.commit()
    return 'Send'


@app.route('/get/<int:id>', methods=['GET'])
@login_required
def get_by_id(id):
    return create_json(Numberplate.query.filter(Numberplate.id>=id))

@app.route('/delete', methods=['POST'])
@login_required
def delete_by_id(id=None):
    if (id is not None):
        Numberplate.query.filter_by(id=id).delete()
    elif (request.form['id']):
        Numberplate.query.filter_by(id=request.form['id']).delete()
    daoPool.sqlDAO.session.commit()
    return 'Delete'

@app.route('/getstat_by_plate', methods=['GET'])
@login_required
def getstat_by_plate(plate=None):
    if (plate is not None):
        plates = Numberplate.query.filter(Numberplate.Licplates==plate)
    elif (request.form['plate']):
        plates = Numberplate.query.filter(Numberplate.Licplates==request.form['plate'])
    return create_json(plates)


# подсчет номеров
# @app.route('/count_plates', methods=['GET'])
# @login_required
# def count_plates(begin=None, end=None):
#     if (begin is not None and end is not None):
#         plates = Numberplate.query.filter(Numberplate.Timestamp>=begin and Numberplate.Timestamp>=end)
#         print(plates)
#     elif (request.form['begin'] and request.form['begin']):
#         plates = Numberplate.query.filter(Numberplate.Timestamp>=request.form['begin'])
#         print(plates)
#     return create_json(plates)

