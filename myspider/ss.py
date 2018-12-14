# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 16:28
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : ss.py
# @Software: PyCharm
from urllib import request
import lxml.html
import random

'''
url = https://free-ss.site/

'''
# proxy
proxy_list = [
    {'http': 'localhost:1080'},
]
proxy = random.choice(proxy_list)
# 构建代理管理器
prox_handler = request.ProxyHandler(proxy)

# 创建请求对象
opener = request.build_opener(prox_handler)

url = 'https://free-ss.site/'
# url = 'http://www.baidu.com'
# url ='https://www.ssrtool.com/tool/free_ssr'
headers = {
    'User_Agent': 'User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'
}
req = request.Request(url, headers=headers)

response = opener.open(req)
html = response.read().decode()
html = lxml.html.etree.HTML(html)
iterm = html.xpath()
print(html)
