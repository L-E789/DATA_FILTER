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

class ALogin(MethodView):
    def post(self):
        login = administrator()
        content = request.get_json()
        login.user = content.get("user")
        password = bytes(str(content.get("password")), encoding = 'utf-8')
        respuesta = login.log_in()
        if (respuesta):
            password_db = bytes(respuesta[0][1], 'utf-8')
            if bcrypt.checkpw(password, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, KEY_TOKEN_AUTH, algorithm='HS256');
                return jsonify({"Status": "Login exitoso", "token": str(encoded_jwt)})  
            return jsonify({"Status": "Login incorrecto 22"}), 400
        else:
            return jsonify({"Status": "Login incorrecto 11"}), 500


class ViewCases(MethodView):
    def post(self):
        Ad = administrator()
        content = request.get_json()
        Ad.status = content.get('status')
        answer = Ad.Count_mesagges()
        return jsonify(answer), 200

class infoView(MethodView):
    def post(self):
        Ad = administrator()
        content = request.get_json()
        Ad.id = content.get('id')
        answer = Ad.info_Const()
        return jsonify(answer), 200

class answer(MethodView):
    def post(self):
        Ad = administrator()
        content = request.get_json()
        print(content)
        Ad.answer = content.get('answer')
        Ad.email = content.get('email')
        Ad.id = int(content.get('id'))
        answer = Ad.answer_consult()
        return jsonify(answer), 200


class enviromentsInfo(MethodView):
    def get(self):
        Ad = administrator()
        answer = Ad.enviromets_info()
        return jsonify(answer), 200

    def post(self):
        Ad = administrator()
        content = request.get_json()
        Ad.id = int(content.get('id'))
        answer = Ad.detail_enviroment()
        return jsonify(answer), 200


class ShowUsers(MethodView):
    def get(self):
        Ad = administrator()
        answer = Ad.show_users()
        return jsonify(answer), 200

    def post(self):
        Ad = administrator()
        content = request.get_json()
        print(content)
        Ad.id = int(content.get('id'))
        answer = Ad.delete_users()
        return jsonify(answer), 200

        
