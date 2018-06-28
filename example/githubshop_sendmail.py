#-*- coding:utf-8 -*-
"""
  简单发个邮件实现
  通知自己关注的商品折扣
"""

import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

today = time.strftime("%Y_%m_%d")
sender = '28asdf9@qq.com'
receivers = ['sdfasdf9@qq.com']
subject = '主人！！GithubShop上您关注的商品降价啦！！\(^o^)/~'

with open('d:\\GithubShop\\{0}\\{0}_discount.txt'.format(today), 'r') as f:
    for line in f.readlines():
        if "Water Bottle" in line:
            msg = line
            message = MIMEText(msg, 'plain', 'utf-8')
            message['From'] = Header(sender, 'utf-8')
            message['To'] = Header(receivers[0], 'utf-8')
            message['Subject'] = Header(subject, 'utf-8')
            
            smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
            smtp.login('28asdf9@qq.com', 'sdsfafdfasdfsadfas')
            smtp.sendmail(sender, receivers, message.as_string())
            smtp.quit()
