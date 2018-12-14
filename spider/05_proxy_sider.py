# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 13:34
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : 05_proxy_sider.py
# @Software: PyCharm


from urllib import request
import random

# 代理
proxy_list = [
    # {'http':'218.18.232.26:8080'},
    # {'http':'58.49.134.202:59095'},
    {'https': '183.63.101.62:53281'},
]
proxy = random.choice(proxy_list)

# 构建代理管理器
proxy_hander = request.ProxyHandler(proxy)

# 创建网络请求对象openner
opener = request.build_opener(proxy_hander)

url = 'http://www.langlang2017.com'

headers = {
    'User_Agent': 'User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'
}

req = request.Request(url, headers=headers)
response = opener.open(req)
html = response.read().decode()
print(req)
print(html)
