#!/usr/bin/env python
#coding=utf-8

import requests
import json,os
from common.log import Log

# 定义请求类
class Interface_Request:

    def __init__(self):
        Current_class = os.path.basename(__file__)
        print(Current_class)
        self.log = Log(Current_class)
        self.session = requests.Session()

    def req_get(self, url, Param, Headers):
        try:
            response = self.session.get(url, params=Param, headers=json.loads(Headers))
            response.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
            # 转换为python类型的字典格式,json包的响应结果，调用json(),转换成python类型
            # print(r.status_code)
            result = response.text
            return result
        except requests.RequestException as e:
            print("请求不能完成:", str(e))
            self.log.error("请求不能完成:%s"%(str(e)))

    def post_kv(self, url, data, headers):
        try:
            response = self.session.post(url, data=data, headers=headers)
            response.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
            # 转换为python类型的字典格式,json包的响应结果，调用json(),转换成python类型
            result = response.text
            # print(result)
            return result
        except requests.RequestException as e:
            print("请求不能完成:", str(e))
            self.log.error("请求不能完成:{}".format(str(e)))

    def post_json(self, url, data, headers):
        try:
            # python类型转化为json类型
            data = json.dumps(data)
            response = self.session.post(url, data=data, headers=headers)
            response.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
            result = response.text
            return result
        except requests.RequestException as e:
            print("请求不能完成:", str(e))
            self.log.error("请求不能完成:%s" % (str(e)))

    def post_file(self, url, files, headers):
        try:
            # 上传文件
            response = self.session.post(url, files=files, headers=headers)
            response.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
            result = response.text
            return result
        except requests.RequestException as e:
            print("请求不能完成:", str(e))
            self.log.error("请求不能完成:%s" % (str(e)))



# #下面为测试代码
# url = "http://p.3.cn/prices/mgets"
# params = {"skuIds":"100004770249","type":"1"}
# headers = {'content-type': 'application/json','User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
# #files = {'file': open('/home/lyb/sjzl.mpg', 'rb')}
# #files = {'file': ('report.jpg', open('/home/lyb/sjzl.mpg', 'rb'))}     #显式的设置文件名
# #files = {'file': ('test.txt', b'Hello Requests.')}     #把字符串当着文件进行上传,必需显式的设置文件名
#
#
# req = Interface_Request()
# print(req.req_get(url,params,headers))
# # req.post_kv(url,params,headers)
# # req.post_json(url,params,headers)
