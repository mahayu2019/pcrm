#!/usr/bin/env python
# coding=utf-8

import requests

key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=key_dict)
print('URL编码:', r.url)
print('响应体:\n', r.text)
