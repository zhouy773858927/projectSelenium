from selenium import webdriver
import os,time

driver = webdriver.Chrome()
file_url = "file:///" + os.path.abspath("upload_file.html")
driver.get(file_url)
time.sleep(3)
#定位上传按钮并且添加本地文件
driver.find_element_by_name("file").send_keys("E:\\百度云\\3月精选视频.txt")
time.sleep(3)