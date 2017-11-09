import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from shanghai import login, Jietu


#流程：一级稽核通过-->二级稽核不通过-->一级稽核不通过-->稽核整改
class Main(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.url = "http://192.168.0.186:6008/saferycom/login.do"
    #稽核用例
    def test_oneJH(self):
        driver = self.driver
        driver.get(self.url)
        login.login(self)#调用登录
        time.sleep(0.5)
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath("//div[@id='menu']/div[9]/div/div[2]/a"))
        element.click()
        time.sleep(1)
        #一级稽核界面
        element = WebDriverWait(driver, 10, 0.5).until(lambda driver: self.driver.find_element_by_xpath("//li[@id='一级稽核']"))
        # element=WebDriverWait(driver, 10, 0.5).until(lambda driver :driver.find_element_by_xpath("//div[9]/div[2]/ul/li[3]"))
        element.click()
        # 旧窗口句柄
        oldhandle = driver.current_window_handle
        driver.switch_to_frame("tabId_1301")
        #工单号
        element = WebDriverWait(driver, 10).until(lambda driver: self.driver.find_element_by_xpath("//*[@id='searchDocId']"))
        element.send_keys("1508309831931")
        time.sleep(2)
        #搜索按钮
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/span[8]/span/a/span"))
        element.click()
        #调用截图方法
        Jietu.jietu(self)
        time.sleep(1)
        # element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//div[@id='menu']/div[9]/div[2]/ul/li[3]"))
        #查看按钮
        element = WebDriverWait(driver, 10).until(lambda driver: self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[12]/div/a"))
        element.click()
        allhandles = driver.window_handles
        #判断当前窗口句柄
        for handle1 in allhandles:
            if handle1 != oldhandle:
                driver.switch_to_window(handle1)
                print("it is now handle1")
                time.sleep(10)
                # 调用截图方法（目前此处截图黑屏）
                Jietu.jietu(self)
                time.sleep(1)
                #稽核通过按钮
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("//a[@id='auditButtonYes']/span/span"))
                element.click()
                #确定按钮
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("/html/body/div[11]/div[2]/div[2]/a[1]/span/span"))
                element.click()
                driver.close()
        #关闭标签页
        time.sleep(1)
        #转到旧句柄
        driver.switch_to_window(oldhandle)
        #二级稽核
        element=WebDriverWait(driver, 10).until(lambda driver :self.driver.find_element_by_xpath("//*[@id='二级稽核']"))
        #element=WebDriverWait(driver, 10, 0.5).until(lambda driver :driver.find_element_by_xpath("//div[9]/div[2]/ul/li[3]"))
        element.click()
        time.sleep(1)
        driver.switch_to_frame("tabId_1303")
        #工单号
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath("//*[@id='searchDocId']"))
        element.send_keys("1508309831931")
        time.sleep(2)
        #搜索按钮
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[3]/span[1]/a/span/span"))
        element.click()
        #查看按钮
        #element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//div[@id='menu']/div[9]/div[2]/ul/li[3]"))
        element=WebDriverWait(driver, 10).until(lambda driver :self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[12]/div/a"))
        element.click()
        allhandles = driver.window_handles
        #判断当前窗口句柄
        for handle2 in allhandles:
            if handle2 != oldhandle:
                driver.switch_to_window(handle2)
                print("it is now handle2")
                #二级稽核不通过按钮
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/a[2]/span/span"))
                element.click()
                #差错类型下拉框
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[1]/div/div[2]/span/span/span"))
                element.click()
                time.sleep(1)
                #下拉框选择
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("/html/body/div[20]/div/ul/li[3]/div/span[3]"))
                element.click()
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath(
                        "/html/body/div[8]/div[2]/div[1]/div/div[2]/span/span/span"))
                element.click()
                #备注
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("//*[@id='reason2']"))
                element.send_keys("ck")
                time.sleep(1)
                #确定按钮
                ##########bug：定位不到提交按钮
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[2]/a[1]/span/span"))
                element.click()
                # case = driver.find_element_by_xpath("//*[@id='audit_state']")
                # print(case.text)
                time.sleep(6)
                driver.close()
        driver.switch_to_window(oldhandle)
        time.sleep(5)
        ##############有bug：二级稽核已经不通过了，但是一级稽核进去时候提示已通过
        # 一级稽核界面
        element = WebDriverWait(driver, 10, 0.5).until(
            lambda driver: self.driver.find_element_by_xpath("//li[@id='一级稽核']"))
        # element=WebDriverWait(driver, 10, 0.5).until(lambda driver :driver.find_element_by_xpath("//div[9]/div[2]/ul/li[3]"))
        element.click()
        time.sleep(1)
        driver.switch_to_frame("tabId_1301")
        # 搜索按钮
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[2]/div[1]/div[2]/span[8]/span/a/span"))
        element.click()
        # element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//div[@id='menu']/div[9]/div[2]/ul/li[3]"))
        # 查看按钮
        element = WebDriverWait(driver, 10).until(lambda driver: self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[12]/div/a"))
        element.click()
        allhandles = driver.window_handles
        # 判断当前窗口句柄
        for handle3 in allhandles:
            if handle3 != oldhandle:
                driver.switch_to_window(handle3)
                print("it is now handle3")
                # 一级稽核不通过按钮
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/a[2]/span/span"))
                element.click()
                # 差错类型下拉框
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath(
                        "/html/body/div[5]/div[2]/div[1]/div/form/div[3]/span/span/span"))
                element.click()
                time.sleep(1)
                # 下拉框选择
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("/html/body/div[11]/div/ul/li[3]/div/span[3]"))
                element.click()
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath(
                        "/html/body/div[5]/div[2]/div[1]/div/form/div[3]/span/span/span"))
                element.click()
                # 备注
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("//*[@id='reason2']"))
                element.send_keys("ck")
                # 确定按钮
                element = WebDriverWait(driver, 10).until(
                    lambda driver: self.driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/a[1]/span"))
                element.click()
                driver.close()
        time.sleep(1)
        # 转到旧句柄
        driver.switch_to_window(oldhandle)
        #稽核整改界面
        element = WebDriverWait(driver ,10).until(
            lambda driver:self.driver.find_element_by_xpath("//*[@id='稽核整改']")
        )
        element.click()
        driver.switch_to_frame("tabId_1305")
        #工单号
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath("//*[@id='searchDocId']"))
        element.send_keys("1508309831931")
        time.sleep(2)
        #搜索按钮
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/span[7]/span/a/span"))
        element.click()
        #查看按钮
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[12]/div/a"))
        element.click()
        driver.switch_to_frame("businessfile")
        #整改表单按钮
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath(
                "/html/body/div[2]/div/div[4]/a[1]/span/span"))
        element.click()
        #整改备注
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath(
                "//*[@id='reason1']"))
        element.send_keys("sk")
        #提交按钮
        element = WebDriverWait(driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath(
                "/html/body/div[6]/div[2]/div[2]/a[1]/span"))
        element.click()
if __name__ == '__main__':
    unittest.main()

# element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//div[@id='menu']/div[9]/div/div[2]/a"))
# element.click()
# time.sleep(1)
# element=WebDriverWait(driver, 10, 0.5).until(lambda driver :driver.find_element_by_xpath("//li[@id='一级稽核']"))
# #element=WebDriverWait(driver, 10, 0.5).until(lambda driver :driver.find_element_by_xpath("//div[9]/div[2]/ul/li[3]"))
# element.click()
# #旧窗口句柄
# oldhandle=driver.current_window_handle
# driver.switch_to_frame("tabId_1301")
# time.sleep(2)
# element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//a[@id='undefined']/span/span"))
# element.click()
# #element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//div[@id='menu']/div[9]/div[2]/ul/li[3]"))
# element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[12]/div/a"))
# element.click()
# allhandles=driver.window_handles
# #判断当前窗口句柄
# for handle1 in allhandles:
#     if handle1 != oldhandle:
#         driver.switch_to_window(handle1)
#         print("it is now handle1")
#         element = WebDriverWait(driver, 10).until(
#             lambda driver: driver.find_element_by_xpath("//a[@id='auditButtonYes']/span/span"))
#         element.click()
#         element = WebDriverWait(driver, 10).until(
#             lambda driver: driver.find_element_by_xpath("/html/body/div[11]/div[2]/div[2]/a[1]/span/span"))
#         element.click()
#         driver.close()
# time.sleep(1)
# #转到旧句柄
# driver.switch_to_window(oldhandle)
# element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//*[@id='二级稽核']"))
# #element=WebDriverWait(driver, 10, 0.5).until(lambda driver :driver.find_element_by_xpath("//div[9]/div[2]/ul/li[3]"))
# element.click()
# time.sleep(1)
# driver.switch_to_frame("tabId_1303")
# time.sleep(2)
# element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[3]/span[1]/a/span/span"))
# element.click()
# #element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("//div[@id='menu']/div[9]/div[2]/ul/li[3]"))
# element=WebDriverWait(driver, 10).until(lambda driver :driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[12]/div/a"))
# element.click()
# allhandles=driver.window_handles
# #判断当前窗口句柄
# for handle2 in allhandles:
#     if handle2 != oldhandle:
#         driver.switch_to_window(handle2)
#         print("it is now handle2")
#         element = WebDriverWait(driver, 10).until(
#             lambda driver: driver.find_element_by_xpath("/html/body/div[2]/div/div[4]/a[1]/span/span"))
#         element.click()
#         element = WebDriverWait(driver, 10).until(
#             lambda driver: driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/a[1]/span/span"))
#         element.click()
