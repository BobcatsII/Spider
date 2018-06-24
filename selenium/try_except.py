from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
try:
    browser.get('https://www.baidu.com')
except TimeoutException as e:
    print('Time Out\n', e)
    
try:
    browser.find_element_by_id('hhhhh')
except NoSuchElementException as e:
    print('No Such\n', e)
finally:
    browser.close()
    
    
    
