from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

browser.get("https://www.zhihu.com/explore")
input = browser.find_element_by_class_name('zu-top-add-question')
print (input.id)
print (input.tag_name)
print (input.location)
print (input.size)
