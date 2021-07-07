from models import conexion
from datetime import timedelta, date, datetime
from bot.send import Send_answer
import datetime


class administrator:
    def __init__(self):
        self.id = 0
        self.name = ''
        self.email = ''
        self.message = ''
        self.answer = ''
        self.viewed = False
        self.status = 0
        self.password = ''
        self.user = ''

    def contact_us(self):
        now = datetime.datetime.now() - datetime.timedelta(hours= 5)
        cmm = conexion.Add("insert into contact_information (name,email,message,shipping_date,viewed) values (%s,%s,%s,%s,%s)", [self.name,self.email,self.message,now,self.viewed])
        if cmm:
            return 'Ok'


    def log_in(self):
        cmm = conexion.search("select user, password from admin where user = %s", [self.user])
        if(cmm):
            return cmm
        return None


    def Count_mesagges(self):
        data = {}
        data['info'] = []
        data['infoS'] = []
        cmm = conexion.View("SELECT viewed,SUM(CASE WHEN viewed = true THEN 1 ELSE 0 END) AS 'Viewed',SUM(CASE WHEN viewed = false THEN 1 ELSE 0 END) AS 'For View' FROM contact_information ")
        if(cmm):
            for i in cmm:
                data['info'].append({'Viewed':int(i[1]),'FView':int(i[2])})
        else:
            return None

        cmc = conexion.search("select id,name,shipping_date from contact_information where viewed = %s order by shipping_date desc", [self.status])
        if(cmc):
            for i in cmc:
                data['infoS'].append({'id':i[0],'name':i[1],'shipping_date':format(i[2])})
            return data
        else:
            return data


    def info_Const(self):
        data = {}
        data['consult'] = []
        cmm = conexion.search("select id,name ,email ,message, viewed, answer_t from contact_information where id = %s", [self.id])
        if(cmm):
            for i in cmm:
                data['consult'].append({'id':i[0],'name':i[1],'email':i[2],'message':i[3], 'viewed':i[4], 'answer_t':i[5]})
            return data['consult']
        else:
            return None


    def answer_consult(self):
        now = datetime.datetime.now() - datetime.timedelta(hours= 5)
        cmm = conexion.Add("update contact_information set  answer_t = %s, answer_d = %s , viewed=1 where id = %s", [self.answer,now,self.id])
        Send_answer(self.email, self.answer)
        if cmm:
            return 'Ok'


    def enviromets_info(self):
        data = {}
        data['info'] = []
        cmm = conexion.View("select e.id,e.name, e.creation_date, u.name, u.surname from environments e inner join users u on e.created_by = u.id;")
        if(cmm):
            for i in cmm:
                data['info'].append({'id':i[0],'environment':i[1],'creation_date':i[2],'name':i[3],'surname':i[4]})
            return data['info']
        else:
            return None


    def detail_enviroment(self):
        data = {}
        data['infoE'] = []
        cmc = conexion.search("select id ,(select count(id_user) from bridge  where id_environments = %s),(select count(enviroment) from clients where enviroment = %s) from environments where id = %s;", [self.id,self.id,self.id])
        if(cmc):
            for i in cmc:
                data['infoE'].append({'users':i[1], 'clients':i[2]})
            return data['infoE']
        else:
            return None


    def show_users(self):
        data = {}
        data['info'] = []
        cmm = conexion.View("select id,name,surname,email,activated from users")
        if(cmm):
            for i in cmm:
                data['info'].append({'id':i[0],'name':i[1],'surname':i[2],'email':i[3],'activated':i[4]})
            return data['info']
        else:
            return None


    def delete_users(self):
        cmm = conexion.Add("delete from users where id = %s", [self.id])
        if cmm:
            return 'Ok'



        
