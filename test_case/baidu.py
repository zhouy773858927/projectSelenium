from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re



class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #百度搜索用例
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + '/')
        time.sleep(2)
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    #百度设置用例
    def test_baidu_set(self):
        driver = self.driver
        #进入搜索主页
        driver.get(self.base_url + '/')
        time.sleep(2)
        above = driver.find_element_by_xpath("//*[@id='u1']/a[8]")
        ActionChains(driver).move_to_element(above).perform()
        time.sleep(2)
        sreach_window = driver.current_window_handle  # 此行代码用来定位当前页面
        time.sleep(2)
        #
        driver.find_element_by_xpath("/html/body/div[2]/div[6]").find_element_by_link_text("搜索设置").click()
        # 设置每页搜索结果为 50 条
        m = driver.find_element_by_name("NR")
        time.sleep(2)
        m.find_element_by_xpath("/html/body/div[2]/div[7]/div/div/div/div[1]/form/div/table/tbody/tr[3]/td[2]/select/option[3]").click()
        time.sleep(2)

    #保存设置的信息
        driver.find_element_by_xpath("/html/body/div[2]/div[7]/div/div/div/div[1]/form/div/table/tbody/tr[7]/td[2]/div[1]/a[1]").click()
        time.sleep(2)
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()
        self.assertEquals([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()

