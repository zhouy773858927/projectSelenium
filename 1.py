from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("selenium")#关于页面元素的定位后面将会详细的介绍，这里通过 id=kw 定位到百度的输入框，并通过键盘方法
#send_keys()向输入框里输入 selenium 多自然语言呀
browser.find_element_by_id("su").click()#这一步通过 id=su 定位的搜索按钮，并向按钮发送单击事件（ click() ）
