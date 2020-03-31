#!/usr/bin/env python
#coding=utf-8

import pymysql,os
from common.readConfig import ReadConfig
from common.log import Log


class MysqlBase:

    log = Log(os.path.basename(__file__))

    def __init__(self):

        #获取数据库配置信息
        conf = ReadConfig()
        mysqlconf = conf.getDBconf()
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=mysqlconf.host, port=int(mysqlconf.port), db=mysqlconf.database,
                                 user=mysqlconf.username,
                                 passwd=mysqlconf.password, charset="utf8",cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            MysqlBase.log.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        recount_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
            cursor.execute(recount_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        #print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()

    @staticmethod
    def testconnect():

        # 打开数据库连接
        conf = ReadConfig()
        mysqlconf = conf.getDBconf()
        try:
            # Connect to the database
            db = pymysql.connect(host=mysqlconf.host, port=int(mysqlconf.port), db=mysqlconf.database,
                                 user=mysqlconf.username,
                                 passwd=mysqlconf.password, charset="utf8")
        except pymysql.err.OperationalError as e:
            MysqlBase.log.error("Mysql Error %d: %s" % (e.args[0], e.args[1]))

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 插入语句
        sql = "INSERT INTO employee(employee_name, \
               , age, sex, income) \
               VALUES ('%s',  %s,  '%s',  %s)" % \
              ('Mohan', 20, 'Female', 2000)
        sqlA = "select * from employee"
        try:
            # 执行sql语句
            cursor.execute(sqlA)
            # 执行sql语句
            # db.commit()

            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                employee_name = row[0]
                age = row[1]
                sex = row[2]
                income = row[3]
                # 打印结果
                print("employee_name=%s,age=%s,sex=%s,income=%s" % \
                      (employee_name, age, sex, income))
        except:
            print("Error: unable to fetch data")
            # 发生错误时回滚
            db.rollback()

        # 关闭数据库连接
        db.close()

if __name__ == '__main__':
    # MysqlBase.testconnect()
    db = MysqlBase()
    table_name = "employee"
    data = {'employee_name':'Kathy','`age`':27,'sex':1,'income':8000,'birthday':'2016-08-20'}

    db.clear(table_name)
    # db.insert(table_name, data)
    # db.close()