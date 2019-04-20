#!/usr/bin/env python
# coding=utf-8

import requests
import bs4
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUnivList(uList, num):
    print("{:^10}\t{:^15}\t{:^10}\t{:^10}".format("排名", "学校", "省份", "总分"))
    for i in range(num):
        u = uList[i]
        print("{:^10}\t{:^15}\t{:^10}\t{:^10}".format(u[0], u[1], u[2], u[3]))


def main():
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 50)


main()
