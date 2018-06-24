import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get('https://www.baidu.com')                  #请求百度页面
browser.execute_script('window.open()')               #打开第一个（标签页）选项卡
print(browser.window_handles)

browser.switch_to_window(browser.window_handles[1])   #打开第二个选项卡（标签页）
browser.get('https://www.taobao.com')                 #请求淘宝页面
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])   #切换到第一个选项卡（标签页）
browser.get('https://python.org')                     #请求python官网页面

