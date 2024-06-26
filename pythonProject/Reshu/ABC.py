from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver. get("https://ecommerce-playground.lambdatest.io/")
search_for_key = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div[2]/input')

search_for_key.send_keys("iphone")

search_btn = driver.find_element(By.XPATH,'//*[@id="search"]/div[2]/button')
search_btn.click()








