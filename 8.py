from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://58.215.200.58:7000/esweb/index.aspx")
driver.find_element_by_id('txtUid').clear()
driver.find_element_by_id("txtUid").send_keys("zhouy")
driver.find_element_by_id("txtPwd").clear()
driver.find_element_by_id("txtPwd").send_keys("zhouy")
#单击按钮
driver.find_element_by_id("btnSubmit").click()
#获得前面title,打印
title = driver.title
print(title)
if title == u"EXCEL服务器2015 WEB版":
    print("title ok")
else:
    print("title on")

#获得前面的url，打印
now_url = driver.current_url
print(now_url)

#拿当前url和预期url对比
if now_url == "http://58.215.200.58:7000/esweb/main/frameset.aspx":
    print("url ok")
else:
    print("url on")

