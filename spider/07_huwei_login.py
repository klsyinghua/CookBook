# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 16:39
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : 07_huwei_login.py
# @Software: PyCharm

'''

url:  https://www.huawei.com/en/accounts/LoginPost
moth: pass

Form Data:

userName: 82537544@qq.com
pwd: k12eYt5d62KT2kExC+uBg4riZbcRKFySpsacacMINAhPQmkkcpw9bH+YZIGz2oUd0iTYIsOZOmGxfRe4LEe2JWXeN0EQWK/xDEyffh09rZcrXmFQeOOLj/oIN3M0ayGydyoSqY3t6NoUX1WkJ48sW3aHrpgo+hxZvNzaKuzONLs=
languages: zh
fromsite: www.huawei.com
authMethod: password

'''

from urllib import request, parse
from http import cookiejar

# 生产cookie对象
cookie = cookiejar.CookieJar()

# cookie 管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# http 请求管理器
http_handler = request.HTTPHandler()

# https 请求管理器
https_handler = request.HTTPSHandler()

# 请求管理器
opener = request.build_opener(cookie_handler, http_handler, https_handler)


# 构建登陆函数
def login(url):
    data = {
        'userName': 'yuxiang000',
        'pwd': 'Huawei12#$',
        'languages': 'zh',
        'fromsite': 'www.huawei.com',
        'authMethod': 'password'
    }
    data = parse.urlencode(data)

    # data数据为bytes
    req = request.Request(url=url, data=bytes(data, "utf-8"))
    content = opener.open(req)
    content = content.read().decode('utf-8')
    print(content)


if __name__ == '__main__':
    url = ' https://www.huawei.com/en/accounts/LoginPost'
    login(url)
