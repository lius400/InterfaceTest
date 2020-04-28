#!/usr/bin/env python
#coding=utf-8

import csv,os

#测试数据封装
class TestData:

    def __init__(self,ID,URL,URI,Param,Dataform,Checkpoint,Headers,Casename):
        self.ID = ID
        self.URL = URL
        self.URI = URI
        self.Param = Param
        self.Dataform = Dataform
        self.Checkpoint = Checkpoint
        self.Headers = Headers
        self.Casename = Casename

class ReadTestData:

    @staticmethod
    def Read():
        csvfile = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "/Data/TestData.csv"
        DataList = []
        with open(csvfile) as f:
            f_csv = csv.DictReader(f)
            for row in f_csv:
                # data = TestData(row['用例编号'], row['URL'], row['URI'], row['参数'], row['参数类型'], row['检查点'], row['headers'],
                #                 row['用例名称'])
                data = {"ID":row['用例编号'],"URL":row['URL'],"URI":row['URI'],"RequestForm":row['请求方法(GET/POST)'],"Param":row['参数'],"File":row['File'],"CheckPoint":row['检查点'],"Headers":row['headers'],"CaseName":row['用例名称'],"LinkedData":row['关联数据']}
                DataList.append(data)
        return DataList

    def Save(self):
        heads=['用例编号','用例名称','URL','URI','请求方法','参数类型','参数','检查点','headers','执行','执行结果','测试结果描述']
        rows = [{'用例编号':2,'用例名称':'海信HZ55E3D-J','URL':'http://p.3.cn','URI':'/prices/mgets','请求方法':'GET','参数类型':'Form','参数':'{"skuIds":"100004048751","type":"1"}','检查点':'J_100004048751','headers':"{'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}",'执行':'YES',}]
        with open(self.csvfile,'a') as f:
            f_csv = csv.DictWriter(f,heads)
            # f_csv.writeheader()
            f_csv.writerows(rows)
