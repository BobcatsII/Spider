from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

browser.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException as e:
    print("NO Logo")
    
browser.switch_to.parent_frame()                        #重新切换回父级Frame
logo = browser.find_element_by_class_name('logo')       #在次获取节点
print (logo)
print(logo.text)

