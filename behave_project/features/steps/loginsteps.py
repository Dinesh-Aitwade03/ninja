from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('lunch chrome')
def chrome1(context):
    context.driver = webdriver.Chrome()

@when('open url')
def openurl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/')


@when('enter username "{user}" and password "{pwd}"')
def setin(context ,user,pwd):
    context.driver.find_element(By.XPATH , '//*[@id="divUsername"]/span').send_keys(user)
    context.driver.find_element(By.XPATH, '//*[@id="divPassword"]/span').send_keys(pwd)


@when('click login button')
def clickbuton(context):
    context.driver.find_element(By.XPATH , '//*[@id="btnLogin"]').click()


@then('user should login')
def logon(context):
    try:
        ttl = context.driver.find_element(By.XPATH , ' //*[@id="content"]/div/div[1]/h1').text
    except:
        context.driver.close()
        assert False
    if ttl == "Dashboard":
        context.driver.close()
        assert True