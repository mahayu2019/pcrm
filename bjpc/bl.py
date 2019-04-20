#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

for sibling in soup.body.descendants:
    print(sibling)

#print(soup.body.contents)
