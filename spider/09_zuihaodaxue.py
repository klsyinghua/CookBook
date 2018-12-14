# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 17:44
# @Author  : Alan Lu
# @Email   : lufan.angel@gmail.com
# @File    : 09_zuihaodaxue.py
# @Software: PyCharm

from urllib import request
import lxml.html

baseurl = 'http://zuihaodaxue.com/zuihaodaxuepaiming2018.html'
response = request.urlopen(baseurl)
html = response.read().decode()

html = lxml.html.etree.HTML(html)

# 选取了/下 tr
items = html.xpath('//tr[@class="alt"]')
for item in items:
    # 排名
    number = item.xpath('./td')[0].text
    # print(number,end='')

    school = item.xpath('.//div[@align="left"]')[0].text
    # print(school,end='')

    address = item.xpath('./td')[2].text

    score = item.xpath('./td')[3].text
    # print(address)
    print(number + "#" * 5 + school + "#" * 5 + address + "#" + score)
