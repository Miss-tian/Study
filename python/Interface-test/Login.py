# -*- coding:utf-8 -*-

_author_ = u'tianxin'

import urllib.parse,string

import requests #先导入包

import json


url = "http://47.104.18.57/btmsapi/btmsOAService/login/pc"

data = {"mobile":"15122222222",
        "userPwd":"78302615c8b79cac8df6d2607f8a83ee"}

headers = {'Content-Type':'application/json'}

r = requests.post(url,json.dumps(data),headers =headers)

print(r.text.encode('utf-8'))






