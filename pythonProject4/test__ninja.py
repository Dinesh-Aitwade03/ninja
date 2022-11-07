from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from collections import OrderedDict
import time
import pytest

class Test_ninja:

    username = 'sctestqa@gr.la'
    password = 'Sct@123'



    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

    # .  Go to " http://tutorialsninja.com/demo/index.php" and click on My Account - -> Login.

    def test_oprnurl(self,setup):
        self.driver = setup
        self.driver.get('http://tutorialsninja.com/demo/index.php')
        self.driver.find_element(By.XPATH,'//a[contains(text(),"My Account")]').click()
        ttl=self.driver.title
        if ttl=='Account Login':
            assert True
        else:
            assert False

    # Sign-In using following credentials on Returning Customer Section:
    #      Username: sctestqa@gr.la
    #   Password:  Sct@123

    def test_login(self,setup):
        self.driver = setup
        self.driver.get('http://tutorialsninja.com/demo/index.php')
        self.driver.find_element(By.XPATH, '//a[contains(text(),"My Account")]').click()
        self.driver.find_element(By.ID,'input-email').clear()
        self.driver.find_element(By.XPATH, '//input[@ID="input-email"]').send_keys(self.username)
        self.driver.find_element(By.NAME,'password').clear()
        self.driver.find_element(By.XPATH, '//input[@ID="input-password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH,'//input[@value="Login"]').click()

    # 	On landing page, hit on Home button to see list of available products on website.
    # 	Scroll down and Featured section, we see a list of products.
    # 	Get the Label and associated Price of those item. Fetch them and sort it as per their
    # price [Low to High] and print it
    # on Console [Label and Price]



    def test_product(self,setup):
        self.driver=setup
        self.driver.get('http://tutorialsninja.com/demo/index.php')
        self.driver.find_element(By.XPATH, '//a[contains(text(),"My Account")]').click()
        self.driver.find_element(By.ID, 'input-email').clear()


        self.driver.find_element(By.XPATH, '//input[@ID="input-email"]').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').clear()
        self.driver.find_element(By.XPATH, '//input[@ID="input-password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//input[@value="Login"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="account-account"]/ul/li[1]/a/i').click()
        # feacher_ele = self.driver.find_element(By.XPATH,'//h3[normalize-space()="Featured"]')
        # self.driver.execute_script('arguments[0].ScrollIntoView();',feacher_ele)
        all_pro = self.driver.find_elements(By.XPATH,'//div[@class="product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12"]')


        proname=self.driver.find_elements(By.XPATH,'//div[@Class="caption"]/h4/a')
        for pro in proname:
            print(pro.text)

        proprice=self.driver.find_elements(By.XPATH,'//span[@class="price-tax"]')
        for pr in proprice:
            print(pr.text)

        dict1= zip(proname,proprice)

        mydict =dict(dict1)
        mydict = OrderedDict(mydict)
        for i,j in mydict.items():
            print(i.text+'  :  '+j.text)