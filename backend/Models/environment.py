from MySQLdb import connections
from models import Conexion
from datetime import datetime
import random

class Environment:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.img = ''
        self.key_code = ''
        self.created_by = ''
        self.state = 0
    
    def create(self):
        now = datetime.now()
        insert = Conexion.Add("insert into environments (img,name,key_code,creation_date,created_by) values (%s,%s,%s,%s,%s)",[self.img,self.name,self.key_code,now,self.created_by])
        consult = Conexion.search("select id from environments where key_code = %s",[self.key_code])
        insert2 = Conexion.Add("insert into bridge (id_user,id_environments,v_admin,linking_date,state) values (%s,%s,%s,%s,%s)",[self.created_by,consult[0][0],1,now,1])

    def show(self):
        data = {}
        data['environment'] = []
        consult = Conexion.search("select e.id,e.img,e.name,e.key_code,e.creation_date, u.name, b.id_user, b.v_admin from users u, environments e, bridge b where e.created_by = u.id and b.id_environments = e.id and b.id_user = %s", [self.id])
        if(consult):
            for i in consult:
                data['environment'].append({'id':i[0],'img':i[1],'name':i[2],'key_code':i[3],'creation_date':format(i[4]),'name_user':i[5],'admin':i[7]})
            return data['environment']
        else:
            return None

    def remove(self):
        deleteClient = Conexion.Add("delete from clients where enviroment = %s",[self.id])
        delete = Conexion.Add("delete from bridge where id_environments = %s",[self.id])
        deleteEnv = Conexion.Add("delete from environments where id = %s",[self.id])
    
    def search_environment(self):
        data = {}
        data['environment'] = []
        consult = Conexion.search("select e.id,e.img,e.name,e.key_code,e.creation_date, u.name, b.id_user, b.v_admin from users u, environments e, bridge b where e.created_by = u.id and b.id_environments = e.id and b.id_user = %s and e.name like %s",[self.id,self.name])
        if(consult):
            for i in consult:
                data['environment'].append({'id':i[0],'img':i[1],'name':i[2],'key_code':i[3],'creation_date':format(i[4]),'name_user':i[5],'admin':i[6]})
            return data['environment']
        else:
            return None

    # manage_users ---------------------------------------------------

    def manega_users_show(self):
        data = {}
        data['manage'] = []
        consult = Conexion.search("select u.name, u.img, b.* from users u, environments e, bridge b where  b.id_user = u.id and e.id = b.id_environments and e.id = %s",[self.id])
        if(consult):
            for i in consult:
                data['manage'].append({'name':i[0],"img":i[1] ,'id':i[2],'v_admin':i[5],'linking_date':format(i[6]),'state':i[7]})
            return data['manage']
        else:
            return None
        
    def manega_users_remove(self):
        consult = Conexion.Add("delete from bridge where id = %s",[self.id])
        return consult
    
    def manage_user_join_by_Code(self):
        now = datetime.now()
        data = {}
        data['manage'] = []
        consult1 = Conexion.search('select count(*) from bridge b, users u, environments e where b.id_user = u.id and b.id_environments = e.id and e.key_code = %s and b.id_user = %s',[self.key_code,self.id])
        if(consult1[0][0] != 0):
            return "stError"
        else:
            consult = Conexion.search('select id from environments where key_code = %s',[self.key_code])
            if(consult):
                consult2 = Conexion.Add('insert into bridge (id_user,id_environments,v_admin,linking_date,state) values (%s,%s,%s,%s,%s)',[int(self.id),int(consult[0][0]),0,now,1])
            else:
                return "stError101"
    
    def manage_search(self):
        data = {}
        data['manage'] = []
        consult = Conexion.search('select u.name,b.* from users u, environments e, bridge b where  b.id_user = u.id and e.id = b.id_environments and e.id = %s and u.name like %s',[self.id, self.name])
        if(consult):
            for i in consult:
                data['manage'].append({'name':i[0],'id':i[1],'v_admin':i[4],'linking_date':format(i[5]),'state':i[6]})
            return data['manage']
        return None
    
    def manage_search_email(self,email):
        data = {}
        data['manage'] = []
        consult = Conexion.View('select email from users')
        if(consult):
            for i in email:
                for j in consult:
                    if(i == j[0]):
                        data['manage'].append(j[0])
                        break
        return data['manage']

    def manage_consult_environments(self,env):
        consult = Conexion.search("select name, key_code from environments where id = %s",[env])
        return consult
    
    def manage_consult_owner(self,own):
        consult = Conexion.search("select name from users where id = %s",[own])
        return consult[0][0]
    
    def manage_change_status(self):
        update = Conexion.Add("update bridge set state = %s where id = %s",[self.state,self.id])
        return None

    # ----------------------------------- main ----------------------------------

    def main_bring_data(self):
        data = {}
        data['main'] = []
        consult = Conexion.search("select name from environments where id = %s",[self.id])
        if(consult):
            for i in consult:
                data['main'].append({'name':i[0]})
        return data['main']
    
    def main_register_client(self,identification,env,name,surname,email,phone,address):
        create = Conexion.Add('insert into clients (identification,enviroment,name,surname,email,phone,address) values (%s,%s,%s,%s,%s,%s,%s)',[identification,env,name,surname,email,phone,address])
        return None

    def main_client_consult(self,consult,id_user,env):
        data = {}
        data['main'] = []
        consult = Conexion.search('select identification,name,surname from clients where identification = %s and enviroment =%s',[consult,env])
        if(consult):
            for i in consult:
                 data['main'].append({'consult':i[0],'name':i[1],'surname':i[2]})
            return data['main']
        return None
