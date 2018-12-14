# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 11:02
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : 02_agent.py
# @Software: PyCharm
from urllib import request
import random

'''
http://www.langlang2017.com/index.html
http://www.langlang2017.com/route.html
http://www.langlang2017.com/FAQ.html
'''


def spidre(url):
    user_agetnt_list = [
        'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'User-Agent:Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'
    ]
    # 随机获去useragent
    user_agetnt = random.choice(user_agetnt_list)
    print(user_agetnt)
    # 创建headers 头部信息
    headers = {
        'User_Agetn': user_agetnt
    }
    # 构建Request请求
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()

    # 构建文件名
    name = url.split('/')
    print(name)
    filename = '' + name[-1]
    print(name)

    # 保存文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    url_list = [
        'http://www.langlang2017.com/index.html',
        'http://www.langlang2017.com/route.html',
        'http://www.langlang2017.com/FAQ.html'
    ]

    for url in url_list:
        spidre(url)
