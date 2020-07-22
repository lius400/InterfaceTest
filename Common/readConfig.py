#! /usr/bin/env python
#coding=utf-8

import xml.dom.minidom as xmldom
import os

#Mysql实体类
class Mysql_Entity:
    @property
    def host(self):
        return self._host
    @host.setter
    def host(self, value):
        self._host = value

    @property
    def username(self):
        return self._username
    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, value):
        self._port = value

    @property
    def database(self):
        return self._database
    @database.setter
    def database(self, value):
        self._database = value

#Mail实体类
class Mail_entity:
    @property
    def host(self):
        return self._host
    @host.setter
    def host(self, value):
        self._host = value

    @property
    def adress(self):
        return self._adress
    @adress.setter
    def adress(self, value):
        self._adress = value

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

    @property
    def port(self):
        return self._port
    @port.setter
    def port(self, value):
        self._port = value

    @property
    def sender(self):
        return self._sender
    @sender.setter
    def sender(self, value):
        self._sender = value

    @property
    def receiver(self):
        return self._receiver
    @receiver.setter
    def receiver(self, value):
        self._receiver = value

class ReadConfig:
    def __init__(self):
        xmlfilepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/config/conf.xml"
        print("xml文件路径：", xmlfilepath)
        # 得到文档对象
        domobj = xmldom.parse(xmlfilepath)
        print("xmldom.parse:", type(domobj))
        # 得到元素对象
        self.elementobj = domobj.documentElement
        print("domobj.documentElement:", type(self.elementobj))

    def getmailconf(self):
        mailentity = Mail_entity()
        # 获得子标签
        subElementObj = self.elementobj.getElementsByTagName("conf")
        print("getElementsByTagName:", type(subElementObj))

        # print(len(subElementObj))
        # # 获得标签属性值
        for subElementObjS in subElementObj:
            if subElementObjS.getAttribute("type") == "Email":
                mailentity.host = subElementObjS.getElementsByTagName('mail_host')[0].firstChild.data
                mailentity.username = subElementObjS.getElementsByTagName('mail_adress')[0].firstChild.data
                mailentity.password = subElementObjS.getElementsByTagName('mail_password')[0].firstChild.data
                mailentity.port = subElementObjS.getElementsByTagName('mail_port')[0].firstChild.data
                mailentity.sender = subElementObjS.getElementsByTagName('sender')[0].firstChild.data
                mailentity.receiver = subElementObjS.getElementsByTagName('receiver')[0].firstChild.data
        return mailentity

    def getDBconf(self):
        mysqlentity = Mysql_Entity()
        # 获得子标签
        subElementObj = self.elementobj.getElementsByTagName("conf")
        print("getElementsByTagName:", type(subElementObj))

        # # 获得标签属性值
        for subElementObjS in subElementObj:
            if subElementObjS.getAttribute("type") == "Mysql":
                mysqlentity.host = subElementObjS.getElementsByTagName('host')[0].firstChild.data
                mysqlentity.username = subElementObjS.getElementsByTagName('username')[0].firstChild.data
                mysqlentity.password = subElementObjS.getElementsByTagName('password')[0].firstChild.data
                mysqlentity.port = subElementObjS.getElementsByTagName('port')[0].firstChild.data
                mysqlentity.database = subElementObjS.getElementsByTagName('database')[0].firstChild.data
        # print(mysqlentity.host)
        # print(mysqlentity.username)
        # print(mysqlentity.password)
        # print(mysqlentity.port)
        # print(mysqlentity.database)
        return mysqlentity

if __name__ == '__main__':
    config = ReadConfig()
    config.getDBconf()