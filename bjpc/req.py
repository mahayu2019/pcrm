#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(demo)
print(soup.a)
print(soup.a.attrs)


