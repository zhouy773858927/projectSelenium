from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://192.168.0.186:6008/saferycom/login.do")
coolie = driver.get_cookies()
print(coolie)
time.sleep(10)
#将用户名密码写入浏览器 cookie
driver.add_cookie({'name':'login_name','value':'admin'})
driver.add_cookie({'name':'login_password','value':'saferycom'})
coolie = driver.get_cookies()
print(coolie)
time.sleep(5)
#再次访问 xxxx 网站，将会自动登录
driver.refresh()#刷新
coolie = driver.get_cookies()
print(coolie)

time.sleep(2)