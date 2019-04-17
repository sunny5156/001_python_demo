#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 18:31
# @Author  : Scheaven
# @File    : post_test.py
# @description: 

import requests
import json

url = "http://111.231.83.141:18890/snapshot/worker"
files = {'file': open('D:/vcd/41.jpg', 'rb')}
para = {"Camer_ID":1,"Worker_ID":100012,"hat":0,"frock":1,"glove":0,"shoe":0,"timestamp":1554978408}
header ={}

r = requests.post(url, files=files,data=para,headers= header)

print('get请求获取的响应结果json类型',r.text)
print("get请求获取响应状态码",r.status_code)
print("get请求获取响应头",r.headers['Content-Type'])

#响应的json数据转换为可被python识别的数据类型
json_r = r.json()
print(json_r)
