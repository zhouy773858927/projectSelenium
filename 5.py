from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

text = driver.find_element_by_id("cp").text#返回百度页面底部备案信息
print(text)

attribute = driver.find_element_by_id("kw").get_attribute('type')#返回元素的属性值，可以是 id、name、type 或元素拥有的其它任意属性
print(attribute)

result = driver.find_element_by_id("kw").is_displayed()#返回元素的结果是否可见，返回结果为 True 或 False
print(result)

size = driver.find_element_by_id("kw").size

print(size)#size打印有问题