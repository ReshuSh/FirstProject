from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = None


def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    driver.quit()
    var = driver.title == "Google"
    var = driver.current_url == "google.com"
    pytest
