from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait



def login(self):
    driver = self.driver
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys("admin")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/input").send_keys("azt_123")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/form/table/tbody/tr[4]/td[2]/input").send_keys("0000")
    driver.find_element_by_xpath("//input[@value=' 登  录']").click()