from flask.views import MethodView
from flask import jsonify, request
from models.devices import dispositivos
from validation.validator import DiviceSchema
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime
import time

class add_dis(MethodView):
    def post(self):
        content = request.get_json()
        datos = DiviceSchema()
        errors = datos.validate(content)
        if errors:
            return errors, 400
        cmm = dispositivos()
        cmm.user = int(content.get("user"))
        cmm.cliente = content.get("cliente")
        cmm.telefono = content.get("telefono")
        cmm.direccion = content.get("direccion")
        cmm.F_ingreso = content.get("F_ingreso")
        cmm.equipo = content.get("equipo")
        cmm.modelo = content.get("modelo")
        cmm.serial = content.get("serial")
        cmm.marca = content.get("marca")
        cmm.Fcompra = content.get("Fcompra")
        cmm.estadoP = content.get("estadoP")
        cmm.accesorios = content.get("accesorios")
        cmm.falla = content.get("falla")
        cmm.diagnostico = content.get("diagnostico")
        cmm.crear_dis()
        return jsonify("Ingreso exitoso"),200
