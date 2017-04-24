from actions import Actions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#点开搜索设置
above = WebDriverWait(driver,   10).until(lambda    driver  : driver.find_element_by_xpath("//*[@id='u1']/a[8]"))
ActionChains(driver).move_to_element(above).perform()
driver.implicitly_wait(30)
sreach_window=driver.current_window_handle #此行代码用来定位当前页面
driver.find_element_by_xpath("/html/body/div[2]/div[6]").find_element_by_link_text("搜索设置").click()

#点击保存设置
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[7]/div/div/div/div[1]/form/div/table/tbody/tr[7]/td[2]/div[1]/a[1]").click()

#获取警告信息
time.sleep(2)
alert = driver.switch_to_alert()

#接收警告信息
# time.sleep(2)
# alert.accept()

#打印警告信息
time.sleep(2)
print("警告信息：%s"%alert.text)



