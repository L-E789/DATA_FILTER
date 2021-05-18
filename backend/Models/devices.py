from models import Conexion
from datetime import datetime

class device:
    def __init__(self):
        self.id = 0 
        self.user = 0
        self.enviroment = 0
        self.gear = ""
        self.standard = ""
        self.serial = ""
        self.Purchase_Date = ""
        self.props = ""
        self.statusDev = ""
        self.Other = ""
        self.status = 0


    def add_device(self):
        now = datetime.now()
        cmm = Conexion.Add("insert into Devices (User,enviroment,gear,standard,serial,Purchase_Date,props,statusDev,Other,status) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [self.user,self.enviroment,self.gear,self.standard,self.serial,now,self.props,self.statusDev,self.Other,self.status])
        if cmm:
            return 'Ok'

    def edit_device(self):
        cmm = Conexion.Add("update Devices set gear = %s, standard = %s, serial = %s, Purchase_Date = %s,props = %s where id = %s", [self.gear,self.standard,self.serial,self.Purchase_Date,self.props,self.id])
        if cmm:
            return 'Ok'
            
#NO LISTA LOS USUARIOS
    def show_device(self):
        data = {}
        data['device'] = []
        cmm = Conexion.Add("select id,gear,standard,serial,Purchase_Date,props,status from Devices where enviroment = %s",[self.enviroment])
        if(cmm):
            for i in cmm:
                data['device'].append({'id':i[0],'gear':i[1],'standard':i[2],'serial':i[3],'Purchase_Date':format(i[4]),'props':i[5],'status':i[6]})
            return data['device']
        else:
            return None


    def change_status(self):
        cmm = Conexion.Add("uptade Devices set status = %s where id = %s", [self.status,self.id])
        if cmm:
            return 'Ok'

    def delete(self):
        cmm = Conexion.Add("delete from Devices where id = %s",[self.id])
        if cmm:
            return 'Ok'