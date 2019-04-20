#!/usr/bin/env python
# coding=utf-8

import requests

r = requests.get('http://www.santostang.com')
print('编码:', r.encoding)
print('状态码:', r.status_code)
print('响应体:', r.text)
