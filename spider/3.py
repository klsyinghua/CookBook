# -*- coding: utf-8 -*-
# @Time    : 10/31/2018 5:06 PM
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : 3.py
# @Software: PyCharm

from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例

cookie = cookiejar.CookieJar()

# 生产cookie管理器
cookie_hanler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 创建https请求管理器
https_handler = request.HTTPSHandler

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_hanler)


def logig():
    '''
    初次登陆，并获去cookie凭证
    :return:
    '''

    url = ''

    # data
    data = {
        'email': '',
        'password': ''
    }

    data = parse.urlencode(data)

    #
    req = request.Request(url, data=data.encode())

    #
    rep = opener.open(req)


def getHomePage():
    url = ''

    rsp = opener.open(url)

    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)


if __name__ == '__main__':
    logig()
    getHomePage()
