import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get("www.taobao.com")
input = browser.find_element_by_id('q')
input.sendkeys('python')
input.sendkeys(Keys.ENTER)
time.sleep(3)
browser.close()
