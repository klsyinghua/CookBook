# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 12:01
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : baidutieba.py
# @Software: PyCharm

from urllib import request
from urllib import parse

url = 'http://tieba.baidu.com/f?'
name = input('请输入贴吧名称')
page = input('请输入贴吧面')

# page 为str 需要转化
for i in range(int(page)):
    qs = {
        'kw': name,
        'pn': i * 50
    }

    qs_data = parse.urlencode(qs)
    print(qs_data)
    url = url + qs_data

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    }

    req = request.Request(url=url, headers=headers)

    response = request.urlopen(req)
    html = response.read().decode()
    print(req)

    filename = '' + name

    with open(filename + '.html', 'w', encoding='utf-8') as f:
        f.write(html)
