

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-10-14 10:46:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from urllib.request import quote
import datetime,time
import random
import hashlib
import hmac
import datetime
import requests
import json
import base64
import binascii

# urlencode(base64_encode(hex2bin(hash_hmac('sha1', $param, $tauth_token_secret))));

class URLClient(object):
    def __init__(self, ak, sk, service, domain, region, use_ssl = False):
        self.ak = ak
        self.sk = sk
        # self.host = service + "." + domain
        self.host = domain
        self.service = service
        self.portocol = "https" if use_ssl else "http"
        self.base_utl = self.portocol + "://" + self.host + "/"
        self.url_api = self.base_utl + "DeviceQvod/getQvodUrl"

    def get_utc_datetime(self):
        now_utc = datetime.datetime.utcnow()
        datetime_utc = now_utc.strftime('%Y%m%dT%H%M%SZ')
        date_utc = now_utc.strftime('%Y%m%d')
        return datetime_utc,date_utc

    def get_auth_in_header(self,auth_time, rand_num):
        auth_str = self.ak + "\n" + str(auth_time) + "\n" + str(rand_num)
        # digest = hmac.new(bytes(self.sk, encoding='utf-8'), bytes(auth_str,encoding='utf-8'), digestmod=hashlib.sha1).hexdigest()
        digest = hmac.new(bytes(self.sk, encoding='utf-8'), bytes(auth_str,encoding='utf-8'), digestmod=hashlib.sha1).hexdigest()
        encrypt_string = base64.b64encode(binascii.a2b_hex(digest))
        authorization  = self.ak + ":" + encrypt_string.decode('utf-8')
        return authorization

    def do_requests(self):
        method ='post'
        canonical_uri = "/"
        encode_uri = quote(canonical_uri, safe="/")
        headers = {}
        auth_time = int(time.time())
        rand_num = random.randint(0, 10000000)
        headers["auth-time"] = str(auth_time)
        headers["rand-num"] = str(rand_num)
        headers["authorization"] = self.get_auth_in_header(auth_time, rand_num)
        body = {
            "product_key": "bf591e0cb091",
            "device_sn": "360M990b367b62182a",
            "start_ts": "1631155313",
            "end_ts":"1631158758"
        }
        re = requests.post(self.url_api, headers=headers, data = body)
        # print(re.status_code)
        # print(re.text)
        # re = requests.get(self.url_api, headers=headers, data=body)
        if re.status_code == 200:
            print("success catch url")
            return 1, json.loads(re.text)["data"]["url"]
        else: return -1 ,""

if __name__ == '__main__':
    ak = "ebe77b5dbe934e0c64aff9b03196e6f7"
    sk = "ddf1cb976c76dd0bf5dae711e15a3d0d"
    service = "test"
    domain = "api-monitor.live.360.cn"
    product_key = "bf591e0cb091"
    region = '/DeviceQvod/getQvodUrl'
    urlC = URLClient(ak,sk,service,domain,region,True)
    rec, video_url = urlC.do_requests()
    if rec ==1 :
        print(video_url)

