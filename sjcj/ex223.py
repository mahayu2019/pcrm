#!/usr/bin/env python
# coding=utf-8

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonscraping.com/pages/page3.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")

for child in soup.find("table", {"id": "giftList"}).children:
    print(child)
