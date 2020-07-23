
import sys, time
sys.path.append('../db_fixture')
from Common.DButil import MysqlBase

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-100000))

# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+10000))



# create data
datas = {
    'employee':[
        {'employee_name': 'Kathy', '`age`': 27, 'sex': 1, 'income': 8000, 'birthday': '2016-08-20'},
    ],
    'sign_guest':[
        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1},
        {'id':2,'realname':'has sign','phone':13511001101,'email':'sign@mail.com','sign':1,'event_id':1},
        {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com','sign':0,'event_id':5},
    ],
}


# Inster table datas
def init_data():
    MysqlBase().init_data(datas)


if __name__ == '__main__':
    init_data()