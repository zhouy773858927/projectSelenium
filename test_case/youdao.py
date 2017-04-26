from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import HTMLTestRunner
import unittest,time,re

class Youdao(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.youdao.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    #有道搜索用例
    def test_youdao_search(self):
        driver = self.driver
        driver.get(self.base_url + '/')

        m = driver.find_element_by_id("border").find_element_by_xpath("//*[@id='translateContent']")
        m.clear()
        m.send_keys(u"虫师")
        driver.find_element_by_xpath("/html/body/div[5]/div/form/button").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        self.assertEquals([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()