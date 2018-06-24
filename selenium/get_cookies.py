from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

browser.get("http://www.zhihu.com/explore")
print (browser.get_cookies())
browser.add_cookie({'name':'name', 'domain':'www.zhihu.com', 'value':'germey'})
print(browser.get_cookies())
browser.delete_all_cookies()
print (browser.get_cookies())
