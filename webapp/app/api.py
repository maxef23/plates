from app import app, db
from app.utils import get_user_id_by_token, get_user_by_token, login_required

from flask import jsonify
from flask import Response, request

import datetime
import locale

from app.model.NumberplateModel import Numberplate
from app.model.UserModel import User
from app.dao import daoPool


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


@app.route('/get', methods=['GET', 'POST'])
@login_required
def get():
    if (request.method == 'GET'):
        return create_json(Numberplate.query.all())
    if (request.method == 'POST'):
        if (request.form['id'] is not None):
            return create_json(Numberplate.query.filter(Numberplate.id>=request.form['id']))


@app.route('/send', methods=['POST'])
@login_required
def send(CamID = None, Timestamp = None, Licplates = None):
    if (request):
        last = Numberplate.query.order_by(Numberplate.id.desc()).first()
        if (last.Licplates == request.form['Licplates'] and int(last.CamID) == int(request.form['CamID'])):
            return Response('Duplicate plate', status=400)
        plate = Numberplate(request.form['CamID'], request.form['Timestamp'], request.form['Licplates'])
    elif (CamID is not None and Timestamp is not None and Licplates is not None):
        plate = Numberplate(CamID, Timestamp, Licplates)
    else:
        return '';
    daoPool.sqlDAO.session.add(plate)
    daoPool.sqlDAO.session.commit()
    return 'Send'


@app.route('/delete', methods=['POST'])
@login_required
def delete_by_id(id=None):
    if (id is not None):
        Numberplate.query.filter_by(id=id).delete()
    elif (request.form['id']):
        Numberplate.query.filter_by(id=request.form['id']).delete()
    daoPool.sqlDAO.session.commit()
    return 'Delete'

@app.route('/getstat_by_plate', methods=['POST'])
@login_required
def getstat_by_plate(plate=None):
    if (plate is not None):
        plates = Numberplate.query.filter(Numberplate.Licplates==plate)
    elif (request.form['plate']):
        plates = Numberplate.query.filter(Numberplate.Licplates==request.form['plate'])
    return create_json(plates)

@app.route('/count_plates', methods=['POST'])
@login_required
def count_plates(begin=None, end=None):
    if (begin is not None and end is not None):
        plates = Numberplate.query.filter_by(Numberplate.Timestamp>=begin, Numberplate.Timestamp<=end)
        print(plates)
    elif (request.form['begin'] and request.form['end']):
        plates = Numberplate.query.filter(Numberplate.Timestamp>=request.form['begin'], Numberplate.Timestamp<=request.form['end'])
        print(plates)
    return create_json(plates)

