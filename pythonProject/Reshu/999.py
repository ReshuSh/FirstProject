import time

import boxes
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.jotform.com/form-templates/admissions-form")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@class='form-textbox'])[1]").send_keys("eee")




