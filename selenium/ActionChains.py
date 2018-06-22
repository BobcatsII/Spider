from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_id('draggable')    #源点
target = browser.find_element_by_id('droppable')    #终点

actions = ActionChains(browser)               
actions.drag_and_drop(source, target)               #drag_and_drop()方法
actions.perform()                                   #执行

