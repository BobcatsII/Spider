import time
from selenium import webdriver
browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.python.com')

browser.back()
time.sleep()
browser.forward()
browser.close()

