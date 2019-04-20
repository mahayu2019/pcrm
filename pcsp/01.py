#!/usr/bin/env python
# coding=utf-8


import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3559.6 Safari/537.36',
    'Host': 'www.santostang.com'}

r = requests.get(link, headers)

soup = BeautifulSoup(r.text, 'lxml')
print(soup.a.attrs)