#!/usr/bin/env python
#coding=utf-8

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","11111111","test" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO employee(first_name, \
       last_name, age, sex, income) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
      ('Mac', 'Mohan', 20, 0, 2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

# 关闭数据库连接
db.close()