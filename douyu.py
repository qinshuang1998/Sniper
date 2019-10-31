#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json

def search_dance(data):
    for it in data:
        if it['icv1'][1] and it['icv1'][1][0]['id'] == 656:
            print('{0} - https://www.douyu.com{1}'.format(it['rn'], it['url']))

url = 'https://www.douyu.com/gapi/rkc/directory/0_0/{0}'
start_page = 1
html = requests.get(url.format(start_page))
res = json.loads(html.text)
total_page = res['data']['pgcnt']
search_dance(res['data']['rl'])
if total_page > 1:
    for i in range(2, total_page + 1):
        html = requests.get(url.format(i))
        res = json.loads(html.text)
        search_dance(res['data']['rl'])