#! /usr/bin/env python
#coding=utf-8

import openpyxl,os
import sys
from common.log import Log
from src import InterfaceTest

sys.path.append("./")


#避免转义,将\写成/
#path = "C:/Users/Administrator/Desktop/liuchao-testcase.xlsx"

class ReadCase:
    def get_case(self,casedir,resultdir):
        log = Log(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'./logs/test.log')
        try:
            #打开excel文件,返回标记位给wb
            wb = openpyxl.load_workbook(casedir)
            log.info("打开测试用例成功!")

            # 获取sheet(第二个sheet)
            sheet = wb.get_sheet_by_name("TestCase")
            print("获取指定的工作表:", sheet.title)
        except BaseException as e:
            log.info("打开测试测试用例失败:"+str(e))


        #for循环遍历case
        for i in range(2,sheet.max_row + 1):
            if sheet.cell(row = i,column = 10).value.replace('\n','').replace('r','') != 'Yes':
                continue

            request_data1 = sheet.cell(row = i,column = 1).value
            print(type(request_data1),request_data1)

            request_data2 = sheet.cell(row = i,column = 2).value
            print(type(request_data2),request_data2)

            request_data3 = sheet.cell(row = i,column = 3).value
            print(type(request_data3),request_data3)

            request_data4 = sheet.cell(row = i,column = 4).value
            print(type(request_data4),request_data4)

            request_data5 = sheet.cell(row = i,column = 5).value
            print(type(request_data5),request_data5)

            request_data6 = sheet.cell(row = i,column = 6).value
            print(type(request_data6),request_data6)

            request_data7 = sheet.cell(row = i,column = 7).value
            #excel里取出来的是字符串,需要用eval函数转换
            #取的是字符串,转换成字典
            request_data7 = eval(request_data7)
            print(type(request_data7),request_data7)


            request_data8 = sheet.cell(row = i,column = 8).value
            print(type(request_data8),request_data8)

            request_data9 = sheet.cell(row = i,column = 9).value
            request_data9 = eval(request_data9)
            print(type(request_data9),request_data9)


            #调用接口类
            # headers = {}
            headers = request_data9
            it = InterfaceTest()
            it.testrequest(request_data3,request_data4,request_data7,request_data5,request_data6,request_data8,headers,i,sheet,request_data1,request_data2,log)

#保存数据,excel另存为
        wb.save(resultdir)


#测试用例地址
#获取上级目录
#print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
#print(os.path.abspath(os.path.dirname(os.getcwd())))
#print(os.path.abspath(os.path.join(os.getcwd(), "..")))

casedirT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\Data"+"\TestData.xlsx"
resultdirT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+"\\result"+"\ResultData.xlsx"
readcase1 = ReadCase()
readcase1.get_case(casedirT,resultdirT)
# # if sheet.cell(row = i,column = 10).value.replace('\n','').replace('r','') != 'Yes':
# #     continue
# request_data1 = sheet.cell(row = i,column = 2).value.replace('\n','').replace('r','')
# #excel里取出来的是字符串,需要用eval函数转换
# print(type(request_data1))
#
# request_data1 = eval(request_data1)
# print(request_data1)
