# -*-coding:utf-8 -*-
import urllib.request
import ssl

req = urllib.request.Request('https://192.168.0.61:8443/japi/v3.0/dfs/user/login')
req.data = b'abc'
# 忽略https证书
context = ssl._create_unverified_context()
ret = urllib.request.urlopen(req, context=context).read()
print(ret)
