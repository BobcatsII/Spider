"""
  分析：
  若已登录，先退出，并清除cookie
  打开github页面，输入用户\密码，打开F12，勾选Preserve Log（显示持续日志）
  点击登录，看到各个请求过程
  打开第一个请求，进入详情页
  请求url: https://github.com/session, 请求方式：post
  继续查看Form Data 和 Headers 两部分
  Headers 包含：Cookies、Host、Origin、Refer、User-Agent等
  Form Data 包含五个字段：commit 固定字符串 Sign in， 
                         utf8 是一个勾选字符， 
                         authenticity_token 是一个Base64 加密字符串，
                         login是用户名，
                         password是密码。
  所以，无法直接构造的内容有cookies和authenticity_token.
  清除cookie，重新登录，发现 Response Headers 里有一个 Set-Cookie 字段。这就是设置Cookie的过程。
  查看网页源码，搜索到authenticity_token，他是一个隐藏式表单元素。
  以上，获取到所有信息，可以实现模拟登录了。
"""


import requests
from lxml import etree

class Login(object):
    def __init__(self):
        self.headers = {
          "Referer": "https://github.com/login",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
          "Host":"github.com"
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.session = requests.Session()
        
    def token(self):
        response = self.session.get(self.login_url)
        html = response.text
        s = etree.HTML(html)
        t = s.xpath('//input[@name="authenticity_token"]')[0]
        token = t.attrib['value']
        print (token)
        return token

    def dynamics(self, html):
        tree = etree.HTML(html)
        items_lst = tree.xpath('//ul/li/div[contains(@class, "width-full")]/a/span[2]/text()')
        items = ','.join(items_lst)
        print (items)

    def login(self, user, passwd):
        post_data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": self.token(),
            "login": user,
            "password": passwd
        }
        res = self.session.post(self.post_url, data=post_data, headers=self.headers)
        print (res.url)
        print (res.status_code)
        if res.status_code == 200:
            return self.dynamics(res.text)
          
if __name__ == "__main__":
    login = Login()
    login.login(user="286@qq.com", passwd="Ln9nan")
