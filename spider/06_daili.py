# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 14:14
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : 06_daili.py
# @Software: PyCharm

from urllib import request

isProxy = input('please input is proxy ? y/n:')
url = 'http://www.langlang2017.com'
proxy_list = [
    {'https': '183.63.101.62:53281'},
]

proxy = request.ProxyHandler(proxy_list[0])

# 无代理

proxy_no = request.ProxyHandler()

opener = request.build_opener(proxy_no)

if isProxy == 'y':
    opener = request.build_opener(proxy)
    print('*' * 10 + 'proxying.....')

req = request.Request(url)
response = opener.open(req)
print(response)
