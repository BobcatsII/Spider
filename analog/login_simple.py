"""
  简单的模拟登陆
"""

import requests
from lxml import html

login_url = "https://github.com/login"
session_url = "https://github.com/session"

req = requests.session()
r = req.get(login_url)
tree = html.fromstring(r.text)
cok = tree.xpath('//input[@name="authenticity_token"]')[0]
authenticity_token = cok.attrib["value"]

data = {
    "commit": "Sign in",
    "utf8": "✓",
    "authenticity_token": authenticity_token,
    "login": "2865@qq.com",
    "password": "Ln9an"
}

resp = req.post(session_url, data=data)
result = html.fromstring(resp.text)
items_lst = result.xpath('//ul/li/div[contains(@class, "width-full")]/a/span[2]/text()')
items = ','.join(items_lst)
print (items)
