#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json

def search_dance(data):
    for it in data:
        if it['imgRecInfo'] and it['imgRecInfo']['type'] == 'isDancing':
            print('{0} - https://www.huya.com/{1}'.format(it['introduction'], it['profileRoom']))

url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page={0}'
start_page = 1
html = requests.get(url.format(start_page))
res = json.loads(html.text)
total_page = res['data']['totalPage']
search_dance(res['data']['datas'])
if total_page > 1:
    for i in range(2, total_page + 1):
        html = requests.get(url.format(i))
        res = json.loads(html.text)
        search_dance(res['data']['datas'])