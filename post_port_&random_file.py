#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 18:31
# @Author  : Scheaven
# @File    : post_test.py
# @description: 

import requests
import random
import string,os
import json,time

url = "http://111.231.83.141:18890/snapshot/worker"
# para = {"Camer_ID":1,"Worker_ID":100012,"hat":0,"frock":1,"glove":0,"shoe":0,"timestamp":1554978408}
# files = {'file': open('D:/vcd/41.jpg', 'rb')}
fileDir = "D:/01_Ientification/02_openvino/2019-4-24/model/logs/host/"
logDir = "D:/01_Ientification/02_openvino/2019-4-24/model/logs/mylog.log"
# file_list =random.sample(os.listdir(fileDir),1000)
header ={}
i = 0
file_ls = open(logDir).readlines()

for line in file_ls:
    temp = line.split(";")
    files = {'file':open(fileDir+str(temp[-1].replace("\n","").split(":")[-1])+".jpg", 'rb')}
    # print()
    para = {"Camer_ID":'00'+str(random.randint(1,4)),"Worker_ID":''.join(random.sample(string.digits,6)),"hat":temp[2].split(":")[-1],"frock":temp[3].split(":")[-1],"glove":random.randint(0,1),"shoe":random.randint(0,1),"timestamp":int(round(time.time()*1000))}
    r = requests.post(url, files=files, data=para, headers=header)
    time.sleep(random.uniform(0.1,0.3))
    i += 1
    print(i)
# r = requests.post(url, files=files,data=para,headers= header)

print('get请求获取的响应结果json类型',r.text)
print("get请求获取响应状态码",r.status_code)
print("get请求获取响应头",r.headers['Content-Type'])

#响应的json数据转换为可被python识别的数据类型
json_r = r.json()
print(json_r)
