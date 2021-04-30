from models import Conexion
from datetime import timedelta, date, datetime

class users:

    def __init__(self):
        self.name = ''
        self.surname = ''
        self.email =''
        self.password = ''
        self.activated = 0
        self.code = ''

    def create_user(self):
        respuesta = Conexion.Add("insert into users (name,surname,email,password,img,activated,code) values (%s,%s,%s,%s,%s,%s,%s);",[self.name,self.surname,self.email,self.password,'img',0,self.code])

    def get_user(self):
        respuesta = Conexion.search("select * from users where email = %s ",[self.email])
        if(respuesta):
            return respuesta
        else:
            return None
    
    def activated_account(self):
        respuesta = Conexion.Add('update users set activated = %s where code = %s',[self.activated, self.code])
    

    def send_email_recover(self):
        respuesta = Conexion.search('select name,email from users where email = %s',[self.email])
        if respuesta:
            for i in respuesta:
                now = datetime.now() + timedelta(hours=24)
                resp = Conexion.Add('update users set code=%s, recovery_date= %s where email = %s',[self.code,now,self.email])
                return i[0]
        else:
            return None
    
    def check_code(self):
        respuesta = Conexion.search('select code, recovery_date from users where code = %s',[self.code])
        if respuesta:
            for i in respuesta:
                now = datetime.now()
                if now.strftime('%Y %m %d %H %M %S') > i[1].strftime('%Y %m %d %H %M %S'):
                    return 'invalid'
                else:
                    return 'valid'
        else: 
            return None
    
    def modification_pass(self):
        now = datetime.now()
        respuesta = Conexion.Add('update users set password = %s, recovery_date = %s where code = %s',[self.password,now,self.code])
        if respuesta:
            return 'Ok'