
from selenium.webdriver.common.by import By


class Loginpage:
    register_xpath = '//*[@id="column-right"]/div/a[2]'



    def __init__(self,driver):
        self.driver = driver


    def loginpagee(self):
        self.driver.find_element(By.XPATH,self.register_xpath).click()