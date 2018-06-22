import time
from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get("www.taobao.com")
lis = browser.find_elements_by_css_selector('.service-db li')
print (lis)
time.sleep(3)
brower.close()
