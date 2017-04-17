from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://58.215.200.58:7000/esweb/index.aspx")

driver.find_element_by_id("txtUid").clear()
driver.find_element_by_id("txtUid").send_keys("zhouy")

driver.find_element_by_id("txtPwd").clear()
driver.find_element_by_id("txtPwd").send_keys("zhouy")
driver.find_element_by_id("btnSubmit").click()
driver.find_element_by_id("btnSubmit").submit()
time.sleep(2)
right = driver.find_elements_by_xpath("//*[@id='btnAdd']")
ActionChains(driver).context_click(right)

#鼠标事件，有问题暂时没明白
