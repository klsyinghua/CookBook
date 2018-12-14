#  -*- coding: utf-8 -*-
#  @Time    : 2018/12/14 21:19
#  @Author  : Alan Lu
#  @Email   : lufan.angel@gmail.com
#  @File    : 10_baidu_fanyi.py
#  @Software: PyCharm

from urllib import request
from urllib import parse
import json

'''
url : https://fanyi.baidu.com/sug
datafrom kw:
'''


def db_spider(content):
    # 参数封装
    data = {
        'kw': content
    }
    # 参数拼接转码
    data = parse.urlencode(data)

    # 请求地址
    baseurl = "https://fanyi.baidu.com/sug"

    # 封装headers
    headers = {
        'Content-Length': len(data),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
    }
    # 封装Request对象
    req = request.Request(url=baseurl, data=bytes(data, encoding='utf-8'), headers=headers)
    #
    response = request.urlopen(req)

    html = response.read().decode()
    # print(html)
    # json格式化数据
    json_data = json.loads(html)
    print(json_data)

    for item in json_data['data']:
        print(item['k'] + item['v'])


if __name__ == '__main__':
    content = input("please put in you  word...: \n")
    db_spider(content)
