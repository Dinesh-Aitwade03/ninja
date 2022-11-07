from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch crome browser')
def lunch_browser(context):
    context.driver=webdriver.Chrome()

@when(u'open orangr hrm home page')
def openHomePage(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@then(u'verify logo present on home page')
def logoOnhomepage(context):
    status=context.driver.find_element(By.XPATH,'//*[@id="divLogo"]/img').is_displayed()
    assert status is True


@then(u'close brouser')
def closebrowser(context):
    context.driver.close()