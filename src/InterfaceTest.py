#!/usr/bin/env python
#coding=utf-8

import requests
import re,sys,os
from common.log import Log
import unittest

sys.path.append("./")
from common.Interface_Request import Interface_Request

class InterfaceTest:

    def testrequest(self,URL,URI,Param,RequestForm,DataForm,CheckPoint,Headers,num,CaseName):
        Current_class = os.path.basename(__file__)
        print(Current_class)
        log = Log(Current_class)
        # 可选
        '''
        Headers = {'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
        Headers = {'Content-Type':'application/json;charset=utf-8'}
        '''
        # 生成请求类的对象
        req = Interface_Request()
        # req_get = req.req_get(url,params = params,Headers = Headers)
        # 请求前缀和接口地址的拼接
        full_url = URL + URI

        # 判断请求类型
        if (RequestForm == 'GET'):
            # 调用请求类的函数,得到返回结果
            self.req_test = req.req_get(full_url, Param, Headers)
        elif (RequestForm == 'POST' and DataForm == 'Form'):
            self.req_test = req.post_kv(full_url, Param, Headers)
        elif (RequestForm == 'POST' and DataForm == 'Json'):
            Headers = {'Content-Type': 'application/json;charset=utf-8'}
            self.req_test = req.post_json(full_url, Param, Headers)
        else:
            print("请求不通过,请检查case用例配置:{0}-{1}".format(num,CaseName))
            log.error("请求不通过,请检查case用例配置:{0}-{1}".format(num,CaseName))
            return "请求不通过,请检查case用例配置:{0}-{1}".format(num,CaseName),''

        # 检查点与响应数据做对比
        if (re.search(CheckPoint, str(self.req_test))):
            log.info("用例编号" + str(num) + " " + CaseName + "接口执行成功")
            return "成功", str(self.req_test)
        else:
            log.error("用例编号" + str(num) + " " + CaseName + "接口执行失败")
            return "失败", str(self.req_test)



# #请求前缀
# url = "http://p.3.cn"
# #接口地址
# uri = "/prices/mgets"
# params = {"skuIds":"100004770249","type":"1"}
# Headers = {}
# #请求类型
# RequestForm = 'GET'
# #数据类型
# dataform = 'json'
# #检查点
# checkpoint = '"id":"J_100004770249"'
#
# it = InterfaceTest()
# it.testrequest(url,uri,params,RequestForm,dataform,checkpoint,Headers)