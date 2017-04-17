from selenium import webdriver
import os

driver = webdriver.Firefox()
file_path = "file:///" + os.path.abspath("checkbox.html")
driver.get(file_path)

#选择页面上所有的 tag name 为 input 的元素(标签)
inputs = driver.find_elements_by_tag_name("input")

#然后从中过滤出 tpye 为 checkbox 的元素，单击勾选
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
 # 打印当前页面上 type 为 checkbox 的个数
print(len(driver.find_elements_by_tag_name("input")))

# 把页面上最后1个 checkbox 的勾给去掉
driver.find_elements_by_tag_name("input").pop().click()