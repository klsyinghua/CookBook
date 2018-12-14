# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 17:07
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : 08_ssl.py
# @Software: PyCharm
from urllib import request
import ssl

# ssl免认证
ssl._create_default_https_context = ssl._create_unverified_context

base_url = 'https://www.csls.cdb.com.cn'

response = request.urlopen(base_url)
html = response.read().decode('GBK')
print(html)
