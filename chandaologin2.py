import time
import datetime
from selenium import webdriver

def func():
    #登录禅道方法
    driver = webdriver.Ie()
    driver.implicitly_wait(10)
    driver.get("http://192.168.0.193/zentao/user-login.html")
    #验证网页是否正常打开，不正常则抛出异常，但不影响程序运行
    try:
        assert '用户登录 - 禅道' ==  driver.title
        print("Assertion test pass.")
    except Exception as e:
        print('Assertion test fail.', format(e))
    driver.find_element_by_id("account").send_keys("zhouyang")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/table/tbody/tr[2]/td/input").send_keys("zhouyang")
    driver.find_element_by_id("submit").click()
    time.sleep(2)
    driver.close()

while True:
    #获取当前计算机时间
    current_time = time.localtime(time.time())
    #约定9点30分0秒运行func方法
    if ((current_time.tm_hour == 9) and (current_time.tm_min == 30) and (current_time.tm_sec == 0)):
        func()
        print("登录成功",current_time)
        time.sleep(1)