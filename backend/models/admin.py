from models import conexion


class administrator:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.email = ''
        self.message = ''
        self.viewed = False
        self.psw = ''

    def contact_us(self):
        cmm = conexion.Add("insert into contact_information (name,email,message,viewed) values (%s,%s,%s,%s)", [self.name,self.email,self.message,self.viewed])
        if cmm:
            return 'Ok'


    def log_in(self):
        data = {}
        data['Lag'] = []
        cmm = conexion.search("select user,password from admin where password", [self.psw])
        if(cmm):
            for i in cmm:
                data['Lag'].append({"user":i[0],'password':i[1]})
        return None