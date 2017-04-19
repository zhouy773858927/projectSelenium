from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_link_text("登录").click()
time.sleep(2)
#获取当前页面
nowhandle = driver.current_window_handle
time.sleep(1)
#打开注册窗口
div = driver.find_element_by_id("TANGRAM__PSP_2__content").find_element_by_class_name("pass-reglink")
div.click()

#获得所有窗口
allhandle = driver.window_handles

#循环判断是否为当前窗口
for handle in allhandle:
    if handle != nowhandle:
        driver.switch_to_window(handle)
        print("now register window!")

        driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("zh773858927")
        driver.find_element_by_id("TANGRAM__PSP_3__phone").send_keys("17315053551")
        driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys("19950909")
        time.sleep(2)


driver.switch_to_window(nowhandle)
driver.find_element_by_id("kw").sednd_keys("注册成功")
time.sleep(3)