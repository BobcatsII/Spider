from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
   首先引入WebDriverWait这个对象，指定最长等待时间，然后调用他的until()方法，传入要等待的条件 expected_conditions。
   比如：传入了 presence_of_element_located 这个条件，代表节点出现的意思，其参数是节点的定位元祖，也就是ID为 q 的节点搜索框。
   效果：在10秒内如果ID是q的节点成功加载出来，就返回该节点，如果超过10秒还没加载出来，抛出异常。
        对于按钮，可以更改等待条件，比如改为 element_to_be_clickable （点击），所以查找按钮时查找CSS选择器为.btn-search,如果
        10秒内他是可点击的（成功加载），就返回这个按钮节点，否则，抛出异常。
   ps:页面的加载会受到网络条件的影响
"""

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get("http://www.taobao.com")
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print (input, button)


