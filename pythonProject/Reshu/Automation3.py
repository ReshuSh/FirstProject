from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = '/path/to/chromedriver'
driver = webdriver.Chrome()


driver.get('https://myntra.com')

# Wait for the page to load
time.sleep(3)

# Find element using XPath
xpath_element = driver.find_element(By.XPATH, "//input[@class = 'desktop-searchBar']")
xpath_element.send_keys('bag')
driver.implicitly_wait(5)


css_selector_element = driver.find_element(By.CSS_SELECTOR, 'input.exampleClass')
css_selector_element.send_keys('Test Input via CSS Selector')


button_xpath = driver.find_element(By.XPATH, '//button[@id="exampleButton"]')
button_xpath.click()


button_css_selector = driver.find_element(By.CSS_SELECTOR, '#exampleButton')
button_css_selector.click()
form = driver.find_element(By.CSS_SELECTOR, 'form.exampleForm')
form.submit()


time.sleep(5)
driver.quit()
