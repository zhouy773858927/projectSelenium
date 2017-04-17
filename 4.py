#http://i.xunlei.com/login.html

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://58.215.200.58:7000/esweb/index.aspx")
time.sleep(2)
driver.find_element_by_id('txtUid').clear()
driver.find_element_by_id("txtUid").send_keys("zhouy")

driver.find_element_by_id("txtPwd").clear()
driver.find_element_by_id("txtPwd").send_keys("zhouy")
#单击按钮
driver.find_element_by_id("btnSubmit").click()

#提交

driver.find_element_by_id("btnSubmit").submit()




