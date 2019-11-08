from app import app, db
from app.utils import get_user_id_by_token, get_user_by_token, login_required

from flask import jsonify
from flask import Response, request

import datetime
import locale

from app.model.NumberplateModel import Numberplate
from app.model.UserModel import User
from app.dao import daoPool

import json

def create_json(array):
    list = []
    for item in array:
        list.append({'id' : item.id, 'CamID' : item.CamID, 'Timestamp' : item.Timestamp, 'Licplates' : item.Licplates})
    return jsonify(list)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    in_login = data['login']
    in_password = data['password']
    current_user = User.query.filter_by(login=in_login).first()
    if current_user is None or not current_user.password == in_password:
        return Response('Логин или пароль не верны', status=406)
    else:
        return jsonify({'token': current_user.generate_auth_token().decode('utf-8')})


@app.route('/get', methods=['GET', 'POST'])
@login_required
def get(current_user):
    data = request.get_json()
    if (request.method == 'GET'):
        return create_json(Numberplate.query.all())
    if (request.method == 'POST'):
        if (data['id'] is not None):
            return create_json(Numberplate.query.filter(Numberplate.id>=data['id']))


@app.route('/send', methods=['POST'])
# @login_required
def send():
    if (request):
        last = Numberplate.query.order_by(Numberplate.id.desc()).first()
        if (last.Licplates == request.form['Licplates'] and int(last.CamID) == int(request.form['CamID'])):
            return Response('Duplicate plate', status=400)
        plate = Numberplate(request.form['CamID'], request.form['Timestamp'], request.form['Licplates'])
        daoPool.sqlDAO.session.add(plate)
        daoPool.sqlDAO.session.commit()
        return 'Send'


@app.route('/delete', methods=['POST'])
@login_required
def delete_by_id(current_user):
    data = request.get_json()
    if (data['id']):
        Numberplate.query.filter_by(id=data['id']).delete()
        daoPool.sqlDAO.session.commit()
        return 'Delete'

@app.route('/getstat_by_plate', methods=['POST'])
@login_required
def getstat_by_plate(current_user):
    data = request.get_json()
    if (data['plate']):
        plates = Numberplate.query.filter(Numberplate.Licplates==data['plate'])
    return create_json(plates)

@app.route('/count_plates', methods=['POST'])
@login_required
def count_plates(current_user):
    data = request.get_json()
    if (data['begin'] and data['end']):
        plates = Numberplate.query.filter(Numberplate.Timestamp>=data['begin'], Numberplate.Timestamp<=data['end'])
    return create_json(plates)

