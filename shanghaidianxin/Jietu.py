from selenium import webdriver
import unittest
import os,sys,time
import HTMLTestRunner

# #登录
# driver =webdriver.Ie()
# current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# current_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# print(current_time )
# print(current_time1 )
# # 必须打印图片路径HTMLTestRunner才能捕获并且生成路径，\image\**\\**.png 是获取路径的条件,必须这样的目录
# #设置存储图片路径，测试结果图片可以按照每天进行区分
#
# #通过if进行断言判断
# driver.get("https://baidu.com/")
# pic_path = 'C:\\Users\\Administrator\\Desktop\\'+ current_time1+'\\' + current_time +'.png'
# print(pic_path)
# time.sleep(5)
# print(driver.title)
# #截取当前url页面的图片，并将截取的图片保存在指定的路劲下面（pic_path），注：一下两种方法都可以
# driver.save_screenshot(pic_path)
# driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\'+ current_time1+'\\' + current_time +'.png')
#
# if u'百度一下，你就知道' == driver.title:
#     print ('Assertion test pass.')
# else:
#      print ('Assertion test fail.')
#
#   #通过try抛出异常进行断言判断
# driver.get("https://baidu.com/")
# driver.save_screenshot(pic_path)
# try:
#     assert  u'百度一下，你就知道' ==  driver.title
#     print ('Assertion test pass.')
# except Exception as e:
#     print ('Assertion test fail.', format(e))
#
# time.sleep(5)
# driver.quit()
def jietu(self):
    driver = self.driver
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print("开始截图",current_time)
    time.sleep(3)
    driver.get_screenshot_as_file("C:\\Users\\Administrator\\Desktop\\jietu\\"+current_time+".png")