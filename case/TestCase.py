#! /usr/bin/env python
#coding=utf-8

import openpyxl,os,sys,unittest
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

        self.interfacetest = InterfaceTest()

    def tearDown(self):
        pass

    @data(*datalist)
    def testJDproduct(self,Data):
        #测试用用例描述
        print("用例名称：{}".format(Data["CaseName"]))
        self.log.info("Headers:%s"%(Data["Headers"]))
        Result,Response = self.interfacetest.testrequest(Data["URL"],Data["URI"],Data["Param"],Data["RequestForm"],Data["File"],Data["CheckPoint"],Data["Headers"],Data["ID"],Data["CaseName"])
        print("Response:%s"%(Response))
        self.assertEqual("成功",Result)