#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2018/6/20 14:01
# @Author : li
# @File   : douban150.py


import os
import requests
from urllib.parse import urlencode
from lxml import etree
from multiprocessing.pool import Pool
import threading

def get_page(page):
    parm = {
        'start': page
    }
    url = 'https://book.douban.com/top250?' + urlencode(parm)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
        }
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
    except requests.ConnectionError as e:
        return "Error", e.args


def get_info(i, html):
    selector  = etree.HTML(html)
    bookname  = selector.xpath('//div/table[{0}]//tr/td/div/a/@title'.format(i))[0]
    score     = selector.xpath('//div/table[{0}]//tr/td/div/span[2]'.format(i))[0].text
    original  = selector.xpath('//div/table[{0}]//tr/td/p[1]'.format(i))[0].text
    brief     = selector.xpath('//div/table[{0}]//tr/td/p/span/text()'.format(i))[0]
    info =  "{0}  {1}  {2}  {3}\n".format(bookname, score, original, brief)

    if not os.path.exists(r'D:\untitled\books'):
        os.mkdir(r'D:\untitled\books')

    with open(r'D:\untitled\books\books.txt', 'a+', encoding='utf-8') as f:
        f.write(info)



def main(page):
    html = get_page(page)
    for i in range(1, 26):
        t = threading.Thread(target=get_info, args=(i, html))
        t.start()


if __name__ == "__main__":
    pool = Pool()
    groups = ([ p for p in range(0, 250, 25)])
    print (groups)
    pool.map(main, groups)
    pool.close()
    pool.join()
