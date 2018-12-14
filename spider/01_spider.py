# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 10:45
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : 01_spider.py.py
# @Software: PyCharm

'''
w3c资料简单爬取
url='http://www.w3school.com.cn/json/index.jsp'
method:get
'''
# from urllib import request
#
# resp = request.urlopen('https://www.baidu.com')
# html = resp.read().decode('gb2312')
# print(html)
from urllib import request, error

try:
    base_url = ''
    response = request.urlopen(base_url)
    content = response.read()
    content = content.deconde()
    print(content)
except error.HTTPError as e:
    print(e)

except error.URLError as e:
    print('url错误异常')
