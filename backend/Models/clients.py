from models import conexion

class client:
    def __init__(self):
        self.id = 0 
        self.enviroment = 0 
        self.name =""
        self.surname =""
        self.phone =""
        self.address =""
        self.email =""


    def add_client(self):
        cmm = conexion.Add("insert into Clients (id,enviroment,email,name,surname,phone,address) values (%s,%s,%s,%s,%s,%s,%s)",[self.id,self.enviroment,self.email,self.name,self.surname,self.phone,self.address])
        if cmm:
            return 'Ok'

    def edit_client(self):
        cmm = conexion.Add("update Clients set enviroment = %s , email = %s, name = %s, surname = &s, phone = &s,address = %s where id = &s", [self.enviroment,self.email,self.name,self.surname,self.phone,self.address,self.id])
        if cmm:
            return 'Ok'

    def show_clients(self):
        data = {}
        data['clients'] = []
        cmm = conexion.Add("select * from Clients where enviroment = %s",[self.enviroment])
        if(cmm):
            for i in cmm:
                data['clients'].append({'id':i[0],'enviroment':i[1],'email':i[2],'name':i[3],'surname':i[4],'phone':i[5],'address':i[6]})
            return data['clients']
        else:
            return None

    def search_clients(self):
        data = {}
        data['clients'] = []
        cmm = conexion.Add("select * from Clients where (enviroment = %s and id = %s)",[self.enviroment, self.id])
        if(cmm):
            for i in cmm:
                data['clients'].append({'id':i[0],'enviroment':i[1],'email':i[2],'name':i[3],'surname':i[4],'phone':i[5],'address':i[6]})
            return data['clients']
        else:
            return None

    def delete_client(self):
        cmm = conexion.Add("delete from clients where (enviroment = %s and id = %s)",[self.enviroment, self.id])
        if cmm:
            return 'Ok'