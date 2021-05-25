from models import conexion
from datetime import timedelta, date, datetime


class device:
    def __init__(self):
        self.id = 0
        self.enviroment = 0
        self.client = 0
        self.user = 0
        self.device = ''
        self.model = ''
        self.brand = ''
        self.serial = ''
        self.accessories = ''
        self.condition = ''
        self.work_to_do = ''
        self.status = 0     

    def count_device(self):
        data = {}
        data['device'] = []
        result = conexion.search('select status, count(*) as amount from devices where environment = %s  group by status',[self.enviroment])
        if(result):
            for i in result:
                data['device'].append({"status":i[0],'amount':i[1]})
            return data['device']
        return None

    def add_device(self):
        now = datetime.now()
        cmm = conexion.Add("insert into devices (client,environment,user,type,model,brand,serial,accessories,conditions,work_to_do,status,admission_date) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", [self.client,self.enviroment,self.user,self.device,self.model,self.brand,self.serial,self.accessories,self.condition,self.work_to_do,1,now])
        if cmm:
            return 'Ok'
    
    def delete(self):
        cmm = conexion.Add("delete from devices where id = %s and environment = %s",[self.id, self.enviroment])
        if cmm:
            return 'Ok'
    
    def more_info_device(self):
        data = {}
        data['device'] = []
        cmm = conexion.search('select d.brand,d.model,d.type,d.accessories,d.admission_date,u.name,c.name from users u, devices d,  clients c  where d.user = u.id and d.client = c.identification and d.id = %s and d.environment = %s',[self.id,self.enviroment])
        if(cmm):
            for i in cmm:
                data['device'].append({'brand':i[0],'model':i[1],'type':i[2],'accessories':i[3],'admission_date':format(i[4]),'user':i[5],'customer_name':i[6]})
            return data['device']
        return None

            
    def show_device(self):
        data = {}
        data['device'] = []
        cmm = conexion.search("select d.id, d.brand,d.model,d.type,d.admission_date,u.name,c.name from users u, devices d,  clients c  where d.user = u.id and d.client = c.identification and d.environment =  %s and status = 1",[self.enviroment])
        if(cmm):
            for i in cmm:
                data['device'].append({'id':i[0],'brand':i[1],'model':i[2],'type':i[3],'admission_date':format(i[4]),'user':i[5],'customer_name':i[6]})
            return data['device']
        else:
            return None

    def get_device(self):
        data = {}
        data['device'] = []
        cmm = conexion.search('select type, model, brand, serial, accessories, conditions, work_to_do from devices where id = %s',[self.id])
        if(cmm):
            for i in cmm:
                data['device'].append({'type':i[0],'model':i[1],'brand':i[2],'serial':i[3],'accessories':i[4],'conditions':i[5],'work_to_do':i[6]})
            return data['device']
        return None

    def edit_device(self):
        cmm = conexion.Add('update devices set type = %s, model = %s, brand = %s, serial = %s, accessories = %s, conditions = %s, work_to_do = %s where id = %s',[self.device,self.model,self.brand,self.serial,self.accessories,self.condition,self.work_to_do,self.id])
        if(cmm):
            return cmm
        else:
            return None
    def change_status(self):
        cmm = conexion.Add("uptade Devices set status = %s where id = %s", [self.status,self.id])
        if cmm:
            return 'Ok'


