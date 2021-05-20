from flask.views import MethodView
from flask import jsonify, request
from models.devices import device
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime
import time

class createdevice(MethodView):
    def post(self):
        Dev = device()
        content = request.get_json()
        Dev.user = int(content.get('user'))
        Dev.enviroment = int(content.get('enviroment'))
        Dev.gear = content.get('gear')
        Dev.standard = content.get('standard')
        Dev.serial = content.get('serial')
        Dev.props = content.get('props')
        Dev.statusDev = content.get('statusDev')
        Dev.Other = content.get('Other')
        Dev.status = int(content.get('status'))
        answer = Dev.add_device()
        return jsonify(answer), 200

class editdevice(MethodView):
    def post(self):
        Dev = device()
        content = request.get_json()
        Dev.gear = content.get('gear')
        Dev.standard = content.get('standard')
        Dev.serial = content.get('serial')
        Dev.Purchase_Date = content.get('Purchase_Date')
        Dev.props = content.get('props')
        Dev.id = content.get('id')
        answer = Dev.edit_device()
        return jsonify(answer), 200

    def get(self):
        Dev = device()
        content = request.get_json()
        Dev.enviroment = content.get('enviroment')
        answer = Dev.show_device()
        if(answer):
            return jsonify(answer),200
        else:
            return jsonify(),400 

class changestatus(MethodView):
    def post(self):
        Dev = device()
        content = request.get_json()
        Dev.status = content.get('status')
        Dev.id = content.get('id')
        answer = Dev.change_status()
        return jsonify(answer), 200

class deletedevice(MethodView):
    def post(self):
        Dev = device() 
        content = request.get_json()
        Dev.id = content.get('id')
        answer = Dev.delete()
        return jsonify(answer), 200

class showpending(MethodView):
    def get(self):
        Dev = device()
        content = request.get_json()
        Dev.enviroment = content.get('enviroment')
        answer = Dev.show_pending()
        if(answer):
            return jsonify(answer),200
        else:
            return jsonify(),400 
        