#!/usr/bin/env python
#coding=utf-8

import requests
import re
import sys

sys.path.append("./")
from common.Interface_Request import Interface_Request

'''
class InterfaceTest(object):
    def 方法名称(self):
        请求类的调用,发送请求,获取响应
        re.search(检查点,响应内容)
        re.search(rro_code:'0',r)#匹配到就返回Ture,没有就返回False
        if re.search(rro_code:'0',r):
            print("xxxxxx")
        else:
            print(xxxxxx)
'''

'''
class InterfaceTest:
    def testGet(self):
        url = "http://v.juhe.cn//d"
        params = {"key":"e711bc6362b3179f5a28de7fd3ee4ace","date":"2016-5-14"}
        headers = {}

        req = Interface_Request()
        req_get = req.req_get(url,params = params,headers = headers)
        print(str(req_get))
        if(re.search("'error_code': 0",str(req_get))):
            print("pass")
        else:
            print("fail")


it = InterfaceTest()
it.testGet()
'''


class InterfaceTest:
    def testrequest(self, url, uri, params, reqform, dataform, checkpoint, headers, i, sheet, num, name, log):
        # 可选
        '''
        headers = {'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
        headers = {'Content-Type':'application/json;charset=utf-8'}
        '''
        # 生成请求类的对象
        req = Interface_Request()
        # req_get = req.req_get(url,params = params,headers = headers)
        # 请求前缀和接口地址的拼接
        full_url = url + uri

        # 判断请求类型
        if (reqform == 'GET'):
            # 调用请求类的函数,得到返回结果
            self.req_test = req.req_get(full_url, params, headers)
        elif (reqform == 'POST' and dataform == 'Form'):
            self.req_test = req.post_kv(full_url, params, headers)
        elif (reqform == 'POST' and dataform == 'Json'):
            headers = {'Content-Type': 'application/json;charset=utf-8'}
            self.req_test = req.post_json(full_url, params, headers)
        else:
            print("请求不通过,请检查case用例配置")
            print(self.req_test)

        # 检查点与响应数据做对比
        if (re.search(checkpoint, str(self.req_test))):
            sheet.cell(row=i, column=11).value = "成功"  # row是通过遍历case类传递的
            sheet.cell(row=i, column=12).value = str(self.req_test)
            log.info("用例编号" + str(num) + " " + name + "接口执行成功")
        else:
            sheet.cell(row=i, column=11).value = "失败"
            sheet.cell(row=i, column=12).value = str(self.req_test)
            log.error("用例编号" + str(num) + " " + name + "接口执行失败")



# #请求前缀
# url = "http://p.3.cn"
# #接口地址
# uri = "/prices/mgets"
# params = {"skuIds":"100004770249","type":"1"}
# headers = {}
# #请求类型
# reqform = 'GET'
# #数据类型
# dataform = 'json'
# #检查点
# checkpoint = '"id":"J_100004770249"'
#
# it = InterfaceTest()
# it.testrequest(url,uri,params,reqform,dataform,checkpoint,headers)