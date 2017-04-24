from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_url = "file:///"+os.path.abspath("drop_down.html")
driver.get(file_url)
time.sleep(2)

#定位下拉框
time.sleep(2)
m = driver.find_element_by_id("ShippingMethod")

#点击下拉框的选项
time.sleep(2)
m.find_element_by_xpath("/html/body/select/option[4]").click()
