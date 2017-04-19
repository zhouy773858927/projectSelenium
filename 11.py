from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#点击登录
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/a[7]").click()
time.sleep(2)
sreach_window=driver.current_window_handle #此行代码用来定位当前页面
time.sleep(1)
#通过二次定位找到用户名输入框
div = driver.find_element_by_id("TANGRAM__PSP_2__content").find_element_by_name("userName")
div.clear()
div.send_keys("username")
#输入登录密码
driver.find_element_by_name("password").send_keys("password")

#点击登录
driver.find_element_by_id("TANGRAM__PSP_8__submit").click()

