from selenium import webdriver
import time,os

driver = webdriver.Chrome()
file_url = "file:///" + os.path.abspath("js.html")
driver.get(file_url)

#通过 JS 隐藏选中的元素
#隐藏文字信息
driver.execute_script('$("#tooltip").fadeOut();')

#隐藏按钮
button = driver.find_element_by_class_name("btn")
driver.execute_script('$(arguments[0]).fadeOut()',button)#arguments[0]指函数输入的参数；这里是button
time.sleep(5)

driver.quit()