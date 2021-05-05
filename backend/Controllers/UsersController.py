from models.Usuarios import *
from flask.views import MethodView
from flask import jsonify, request
from config import KEY_TOKEN_AUTH
from bot.send import ActivarCuenta, RecuperarContrasena
import random
import datetime
import time
import bcrypt
import jwt


class Register(MethodView):

    def post(self):
        content = request.get_json()
        name = content.get("name")
        surname = content.get("surname")
        email = content.get("email")
        password = content.get("password")
        validatepassword = content.get("validatepassword")
        register = users()
        if password == validatepassword:
            salt = bcrypt.gensalt()
            register.password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
            register.name = name
            register.surname = surname
            register.email = email
            register.code = random.randint(1000000000,9999999999)
            ActivarCuenta(register.email,register.code)
            respuesta = register.create_user()
            return jsonify(), 200
        return jsonify(), 500


class ValidateAccount(MethodView):
    def get(self,id):
        login = users()
        login.activated = 1
        login.code = str(id)
        respuesta = login.activated_account()
        return jsonify(),200

class SentRecoverPassword(MethodView):
    def post(self):
        content = request.get_json()
        recover = users()
        recover.email = content.get('email')
        recover.code = random.randint(1000000000,9999999999)
        respuesta = recover.send_email_recover()
        if(respuesta):
            RecuperarContrasena(recover.email,recover.code)
            return jsonify(), 200
        return jsonify(), 400

class RecoverPasssword(MethodView):
    def get(self,id):
        recover = users()
        recover.code = str(id)
        check = recover.check_code()
        if check:
            if check == 'valid':
                return jsonify({'codestatus':True,'code':recover.code}), 200
            else:
                return jsonify({'codestatus':False}), 200
        else:
            return jsonify(), 404

class ModificationPassword(MethodView):
    def post(self):
        content = request.get_json()
        recover = users()
        password = content.get('password')
        validatepassword = content.get('validatepassword')
        if(password == validatepassword):
            password = content.get('password')
            salt = bcrypt.gensalt()
            recover.password = bcrypt.hashpw(bytes(str(password), encoding= 'utf-8'), salt)
            recover.code = content.get('code')
            check = recover.modification_pass()
            if check:
                return jsonify({"modifi":True}),200
            else:
                return jsonify({"modifi":False}),400
        else:
            return jsonify(), 400

class Login(MethodView):
    def post(self):
        login = users()
        content = request.get_json()
        login.email = content.get("email")
        password = bytes(str(content.get("password")), encoding = 'utf-8')
        respuesta = login.get_user()
        if (respuesta):
            password_db = bytes(respuesta[0][4], 'utf-8')
            nombres = respuesta[0][1]
            if bcrypt.checkpw(password, password_db):
                encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10000), 'id':respuesta[0][0] ,'email': respuesta[0][3]}, KEY_TOKEN_AUTH , algorithm='HS256')
                return jsonify({"Status": "Login exitoso", "token": str(encoded_jwt),'name': respuesta[0][1], 'surname': respuesta[0][2], 'activated': respuesta[0][6]})  
            return jsonify({"Status": "Login incorrecto 22"}), 400
        else:
            return jsonify({"Status": "Login incorrecto 11"}), 500
    