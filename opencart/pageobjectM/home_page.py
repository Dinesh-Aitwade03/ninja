from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
from selenium.webdriver import ActionChains

class Homepage:
    myacount_xpath = '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a/span'

    def __init__(self,driver):
        self.driver = driver


    def myacount(self):
        ele = self.driver.find_element(By.XPATH,self.myacount_xpath)
        obj = Select(ele)
        obj.select_by_index(1)
