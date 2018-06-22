import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get("www.taobao.com")
input = browser.find_element_by_id('q')
input.send_keys('iphone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()
