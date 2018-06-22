from selenium import webdriver

browser = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

browser.get("https://www.zhihu.com/explore")
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')  #将进度条拉到最下面
browser.execute_script('alert("To Bottom")')                              #弹出警告提示框

