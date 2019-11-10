#! /usr/bin/env python
#coding=utf-8
import sys

sys.path.append("./")
from case.TestCase import ReadCase

sys.path.append("/common")
from common.sendMail import SendMail

path1 = "C:/Users/Administrator/Desktop/接口自动化测试/case/-testcase.xlsx"
path2 = "C:/Users/Administrator/Desktop/接口自动化测试/report/-testreport.xlsx"

rc = ReadCase()
rc.get_case(path1,path2)


sender = 'lius400@163.com'
receiver = 'lius400@163.com'
title = '测试文件'

attach_jpg = 'C:/Users/Administrator/Desktop/接口自动化测试/report/接口测试流程图.jpg'

mail = SendMail()
mail.send_mail(sender,receiver,title,path2,attach_jpg)
print("成功")