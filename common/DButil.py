#!/usr/bin/env python
#coding=utf-8

import pymysql
from common.readConfig import ReadConfig


class MysqlBase:

    def testconnect(self):

        # 打开数据库连接
        conf = ReadConfig()
        self.mysqlconf = conf.getDBconf()
        # db = pymysql.connect("localhost","root","11111111","test" )
        db = pymysql.connect(host=self.mysqlconf.host, port=int(self.mysqlconf.port), db=self.mysqlconf.database, user=self.mysqlconf.username,
                             passwd=self.mysqlconf.password, charset="utf8")

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

