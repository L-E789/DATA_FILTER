from flask.views import MethodView
from flask import jsonify, request
from models.admin import administrator
from config import KEY_TOKEN_AUTH
import random
import datetime
import time
import bcrypt
import jwt



class ContactUs(MethodView):
    def post(self):
        Ad = administrator()
        content = request.get_json()
        Ad.name = content.get('name')
        Ad.email = content.get('email')
        Ad.message = content.get('message')
        Ad.viewed = False
        answer = Ad.contact_us()
        return jsonify(answer), 200

class Login(MethodView):
    def post(self):
        login = administrator()
        content = request.get_json()
        login.psw = bytes(str(content.get("psw")), encoding = 'utf-8')
        respuesta = login.log_in()
        if (respuesta):
            password_db = bytes(respuesta[0][1], 'utf-8')
            if bcrypt.checkpw(login.psw, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, KEY_TOKEN_AUTH, algorithm='HS256');
                return jsonify({"Status": "Login exitoso", "token": str(encoded_jwt)})  
            return jsonify({"Status": "Login incorrecto 22"}), 400
        else:
            return jsonify({"Status": "Login incorrecto 11"}), 500