#! /usr/bin/env python
#coding=utf-8
import sys,os

sys.path.append("./")
from case.TestCase import ReadCase

# sys.path.append("/common")
from common.sendMail import SendMail
from common.readConfig import ReadConfig

casedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"/InterfaceTest/Data/TestData.xlsx"
resultdir =  os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"/InterfaceTest/result/ResultData.xlsx"

rc = ReadCase()
rc.get_case(casedir,resultdir)


mailconf = ReadConfig().getmailconf()
title = '测试文件'

attach_jpg = 'C:/Users/Administrator/Desktop/接口自动化测试/report/接口测试流程图.jpg'

mail = SendMail()
mail.send_mail(mailconf.host,mailconf.port,mailconf.username,mailconf.password,mailconf.sender,mailconf.receiver,title,resultdir,attach_jpg)
print("成功")