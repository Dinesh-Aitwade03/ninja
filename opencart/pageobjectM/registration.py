from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By



class Registration_page:
    first_name_id = 'input-firstname'
    last_name_id = 'input-lastname'
    E_mail_id = 'input-email'
    passworld_ID = 'input-password'
    subscribe_NO_id = 'input-newsletter-no'
    subscribe_YES_id = 'input-newsletter-yes'
    privacy_policy_id = 'agree'
    continue_xpath = '//*[@id="form-register"]/div/div/button'




    def __init__(self,driver):
        self.driver = driver

    def registration(self,fname,lname,email,password):
        self.driver.find_element(By.ID,self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(fname)
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(lname)
        self.driver.find_element(By.ID, self.E_mail_id).clear()
        self.driver.find_element(By.ID, self.E_mail_id).send_keys(email)
        self.driver.find_element(By.ID, self.passworld_ID).clear()
        self.driver.find_element(By.ID, self.passworld_ID).send_keys(password)
        if self.driver.find_element(By.ID,self.subscribe_NO_id).is_selected():
            pass
        else:
            self.driver.find_element(By.ID,self.subscribe_YES_id).click()

        self.driver.find_element(By.ID,self.privacy_policy_id).click()
        self.driver.find_element(By.XPATH,self.continue_xpath).click()



