#! /usr/bin/env python
#coding=utf-8

import xml.dom.minidom as xmldom
import os
from common.sendMail import Mail_entity


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
        # 获得子标签
        mail = Mail_entity()
        subElementObj = self.elementobj.getElementsByTagName("conf")
        print("getElementsByTagName:", type(subElementObj))

        # print(len(subElementObj))
        # # 获得标签属性值
        for subElementObjS in subElementObj:
            if subElementObjS.getAttribute("type") == "Email":
                mail.host = subElementObjS.getElementsByTagName('mail_host')[0].firstChild.data
                mail.username = subElementObjS.getElementsByTagName('mail_adress')[0].firstChild.data
                mail.password = subElementObjS.getElementsByTagName('mail_password')[0].firstChild.data
                mail.port = subElementObjS.getElementsByTagName('mail_port')[0].firstChild.data
                mail.sender = subElementObjS.getElementsByTagName('sender')[0].firstChild.data
                mail.receiver = subElementObjS.getElementsByTagName('receiver')[0].firstChild.data
        return mail

    def getDBconf(self):
        pass