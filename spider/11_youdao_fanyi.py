#  -*- coding: utf-8 -*-
#  @Time    : 2018/12/14 21:47
#  @Author  : Alan Lu
#  @Email   : lufan.angel@gmail.com
#  @File    : 11_youdao_fanyi.py
#  @Software: PyCharm

from urllib import request, parse
import time
import json
import hashlib
import random


def getMD5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding='utf-8'))
    sgin = md5.hexdigest()

    return sgin


def youdao_fanyi(content):
    base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    t = int(time.time() * 1000) + random.randint(0, 10)

    # md5("fanyideskweb" + e + i + "p09@Bn{h02_BIEe]$P^nG")
    new_sign = "fanyideskweb" + str(t) + content + "p09@Bn{h02_BIEe]$P^nG"
    data = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': t,
        'sign': getMD5(new_sign),
        'ts': '1544797763828',
        'bv': '6dfac01e4ee085fbf06475a5a3c2a9c2',
        'doctype': 'json',
        'vsersion': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    # url拼接转码
    data = parse.urlencode(data)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1824293073@116.238.238.98; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; _ntes_nnid=eed64a793b5bcecf8afbd0ee2c1f404f,1544707978027; OUTFOX_SEARCH_USER_ID_NCOO=674867045.7508794; ANTICSRF=8b9e18d7fe0f9ee091d25b76da91b23b; JSESSIONID=aaadAyOJt3VyebP-q_SEw; DICT_FORCE=true; DICT_SESS=v2|e6WV6cFvmkEnMOfkLQuRzY0MQy0MOm0J4hfwLPMJL0g4nMUWRMg40YW0LQBh4PB0JShLQLkfeuRwBO4JFO4TL0lWRLlmOLOA0; DICT_PERS=v2|urstoken||DICT||web||-1||1544798613584||116.238.238.98||klsyinghua@163.com||PFk4eBkfkERquOMTuhL6F0p4kfQu6MQS0YWnLUW0HQZ0kMOfwL0MlfRzAhMlWP4zM0J4nHgu64gF0wZ0HOfPMeZ0; DICT_LOGIN=3||1544798613595; ___rl__test__cookies=1544798616873",
        "DNT": "1",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    # 封装request对象
    req = request.Request(url=base_url, data=bytes(data, encoding='utf-8'), headers=headers)

    # request 请求
    response = request.urlopen(req)
    html = response.read().decode()
    json_data = json.loads(html)
    sr_dict = json_data['smartResult']
    iterms = sr_dict['entries']
    for iterm in iterms:
        print(iterm)


if __name__ == "__main__":
    content = input("请输入您要查询的内容：")
    youdao_fanyi(content)
