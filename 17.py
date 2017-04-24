from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#将滚动条拉到最底下
js = "var q = document.body.scrollTop=10000 "
driver.execute_script(js)
time.sleep(3)

#将滚动条拉到最上
js_ = "var q = document.body.scrollTop=0 "
driver.execute_script(js_)
time.sleep(3)


driver.quit()