from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#print("浏览器最大化")
#driver.maximize_window()#将浏览器最大化显示

print("浏览器宽480，高800")
driver.set_window_size(480,800)
