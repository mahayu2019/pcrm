#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonscraping.com/pages/warandpeace.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

'''
P15对应查阅
findAll(释义)-->finaAll(tag,attributes,recyrsive,text,limit,keywords)
    tag--一个或多个标签组成的标签列表,eg:.findAll({"h1","h2",...})
    attributes--用一个py字典封装一个标签的若干属性和对应的属性值,如下代码class部分
'''

namelist = soup.findAll("span", {"class": "green"})
for name in namelist:
    print(name.get_text())  # get_text()返回去除所有标签的纯文本
