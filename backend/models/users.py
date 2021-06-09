from models import conexion
from datetime import timedelta, date, datetime

class users:

    def __init__(self):
        self.id = 0
        self.name = ''
        self.surname = ''
        self.img = ''
        self.email =''
        self.password = ''
        self.activated = 0
        self.code = ''
        self.env = 0

    def create_user(self):
        respuesta = conexion.Add("insert into users (name,surname,email,password,img,activated,code) values (%s,%s,%s,%s,%s,%s,%s);",[self.name,self.surname,self.email,self.password,"https://firebasestorage.googleapis.com/v0/b/datafilter-32b92.appspot.com/o/profile%2Fpngegg.png?alt=media&token=3f31a154-ef66-487c-abfd-962b3c349e88",0,self.code])

    def get_user(self):
        respuesta = conexion.search("select * from users where email = %s ",[self.email])
        if(respuesta):
            return respuesta
        else:
            return None
    
    def activated_account(self):
        respuesta = conexion.Add('update users set activated = %s where code = %s',[self.activated, self.code])
    

    def send_email_recover(self):
        respuesta = conexion.search('select name,email from users where email = %s',[self.email])
        if respuesta:
            for i in respuesta:
                now = datetime.now() + timedelta(hours=24)
                resp = conexion.Add('update users set code=%s, recovery_date= %s where email = %s',[self.code,now,self.email])
                return i[0]
        else:
            return None
    
    def check_code(self):
        respuesta = conexion.search('select code, recovery_date from users where code = %s',[self.code])
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
        respuesta = conexion.Add('update users set password = %s, recovery_date = %s where code = %s',[self.password,now,self.code])
        if respuesta:
            return 'Ok'

#--------------------------profile--------------------------------------------------------------------------------
    def bring_profile(self):
        data = {}
        data['profile'] = []
        consult = conexion.search('select name, surname, email, img from users where id = %s',[self.id])
        if(consult):
            for i in consult:
                data['profile'].append({'name':i[0],'surname':i[1],'email':i[2], 'img':i[3]})
            return data['profile']
        else:
            return None

    def save_picture(self):
        update = conexion.Add("update users set img = %s where id = %s",[self.img,self.id])
        return 'Ok'


    def edit_name(self):
        update = conexion.Add('update users set name = %s, surname = %s where id = %s',[self.name,self.surname,self.id])
        if update:
            return 'Ok'

    def change_password(self):
        update = conexion.Add('update users set password = %s where id = %s',[self.password,self.id])
        if update:
            return 'Ok'

    def reportG(self):
        data = {}
        data['infoG'] = []
        data['infoU'] = []
        data['infoC'] = []
        data['devices'] = []
        #info general
        cmc = conexion.search("select name, creation_date from environments where id = %s", [self.id])
        if(cmc):
            for i in cmc:
                data['infoG'].append({'name':i[0],'creation_date':format(i[1])})
        else:
            return None
        #conteo 1
        ccm = conexion.search("select count(id_user) from bridge where id_environments =%s", [self.id])
        if(ccm):
            for i in ccm:
                data['infoU'].append({'users':i[0]})
        else:
            return None
        #conteo 2
        ccc = conexion.search("select count(enviroment) from clients where enviroment = %s", [self.id])
        if(ccc):
            for i in ccc:
                data['infoC'].append({'clients':i[0]})
        else:
            return None

        dt = '%Y %M'
        cmm = conexion.search("SELECT DISTINCT DATE_FORMAT(admission_date, %s),SUM(CASE WHEN status = 1 THEN 1 ELSE 0 END) AS 'penging',SUM(CASE WHEN status = 2 THEN 1 ELSE 0 END) AS 'course',SUM(CASE WHEN status = 3 THEN 1 ELSE 0 END) AS 'finished'FROM devices where environment = %s ", [dt,self.id])
        if(cmm[0][0] != None):
            if(cmm):
                for i in cmm:
                    data['devices'].append({'date':format(i[0]),'pending':int(i[1]),'course':int(i[2]), 'finished':int(i[3])}) 
                return data   
            else:
                return None
        else:
            return None
