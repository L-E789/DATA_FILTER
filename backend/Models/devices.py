from models import Conexion


class dispositivos:
    def __init__(self):
        self.user = 0
        self.cliente =""
        self.telefono =""
        self.direccion =""
        self.F_ingreso =""
        self.equipo =""
        self.modelo =""
        self.serial =""
        self.marca =""
        self.Fcompra = ""
        self.estadoP = ""
        self.accesorios = ""
        self.falla = ""
        self.diagnostico = ""


    def crear_dis(self):
        cmm = Conexion.Add("insert into dispositivos(User,Cliente,telefono,Direccion,FechaIngreso,Equipo,Modelo,serial,Marca,FCompra,Accesorios,EstadoProduc,falla,Diagnostico) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.user,self.cliente,self.telefono,self.direccion,self.F_ingreso,self.equipo,self.modelo,self.serial,self.marca,self.Fcompra,self.estadoP,self.accesorios,self.falla,self.diagnostico))
        