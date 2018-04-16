import time
import datetime
from selenium import webdriver

def func():
    #登录禅道方法
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get("http://192.168.0.193/zentao")
    #验证网页是否正常打开，不正常则抛出异常，但不影响程序运行
    try:
        assert '用户登录 - 禅道' ==  driver.title
        print("Assertion test pass.",time.strftime('%Y-%m-%d %H:%M:%S'))
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
    print(current_time)
    #每1小时获取次本地计算机时间
    time.sleep(3600)
    #约定每天14时一小时内校检一次，登录成功打印
    if ((18<current_time.tm_hour<=19 ) and (0<=current_time.tm_min<=60) and (0<=current_time.tm_sec<=60)):
        func()
        print("禅道在%s时登录成功" %time.strftime('%Y-%m-%d %H:%M:%S'))
        time.sleep(1)