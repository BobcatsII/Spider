from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.implicitly_wait(10)       #隐式等待
browser.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
logo = browser.find_element_by_class_name('logo')
print (logo.text)


