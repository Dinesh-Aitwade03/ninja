from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
