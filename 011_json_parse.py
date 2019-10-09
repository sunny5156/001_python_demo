#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 19:48
# @Author  : Scheaven
# @File    :  002_json_parse.py
# @description: json文件解析
import json

with open('results.json', 'r') as jsonfile:
    json_string = json.load(jsonfile)
    print(json.dumps(json_string,indent=2,ensure_ascii=False))