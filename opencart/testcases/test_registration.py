from selenium import webdriver
import pytest
from pageobjectM.home_page import Homepage
from pageobjectM.loginpage import Loginpage
from pageobjectM.registration import Registration_page

class Test_registration:
    fname = 'Dinesh'
    lname = 'AItwade'
    email = 'aitwadedinesh@gmail.com'
    password = '1234'
    baseurl = 'https://demo.opencart.com/'

    def test_registration(self,setup):

        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(25)
        self.hp = Homepage(self.driver)
        self.hp.myacount()
        # self.lp = Loginpage(self.driver)
        # self.lp.loginpagee()
        self.rg = Registration_page(self.driver)
        self.rg.registration(self.fname,self.lname,self.email,self.password)

