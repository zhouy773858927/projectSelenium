from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait


def login(self):
    driver = self.driver
    driver.find_element_by_id("login_name").send_keys("admin")
    driver.find_element_by_id("login_password").send_keys("saferycom")
    time.sleep(10)
    driver.find_element_by_xpath("//input[@value=' 登  录']").click()