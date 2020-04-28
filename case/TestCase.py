#! /usr/bin/env python
#coding=utf-8

import openpyxl,os,sys,unittest,re
from common.log import Log
from ddt import ddt,data
from src.InterfaceTest import InterfaceTest
from common.ReadTestData import ReadTestData


sys.path.append("./")


datalist = ReadTestData().Read()

@ddt
class TestCase(unittest.TestCase):

    def setUp(self):
        Current_class = os.path.basename(__file__)
        print(Current_class)
        self.log = Log(Current_class)
        #关联参数存储字典
        self.OverallData = dict()
        #关联参数生成
        self.LinkedValue = None

        self.interfacetest = InterfaceTest()

    def tearDown(self):
        pass

    @data(*datalist)
    def testJDproduct(self,Data):
        #测试用用例描述
        Response,Result = None,None
        print("用例名称：{}".format(Data["CaseName"]))
        print("LinkedData" + Data["LinkedData"])
        if(Data["LinkedData"] != ''):
            self.LinkedValue = str(Data["LinkedData"])+"="+self.OverallData[str(Data["LinkedData"])]
        self.log.info("Headers:%s"%(Data["Headers"]))
        if(self.LinkedValue != None):
            Result, Response = self.interfacetest.testrequest(Data["URL"], Data["URI"],
                                                              Data["Param"] + self.LinkedValue, Data["RequestForm"],
                                                              Data["File"], Data["CheckPoint"], Data["Headers"],
                                                              Data["ID"], Data["CaseName"])
        else:
            Result, Response = self.interfacetest.testrequest(Data["URL"], Data["URI"],Data["Param"],Data["RequestForm"],Data["File"], Data["CheckPoint"], Data["Headers"],Data["ID"], Data["CaseName"])
        # print("Response:%s"%(Response))
        if( re.findall(r"<td>(.*?)</td>",Response) != None):
            self.OverallData["id"] = re.findall(r"<td>(.*?)</td>", Response[0])
        self.assertEqual("成功",Result)