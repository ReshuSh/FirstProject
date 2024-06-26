from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set the path to the WebDriver
driver_path = '/path/to/chromedriver'

# Initialize the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

try:
    # Open the web page
    driver.get('https://demoqa.com/automation-practice-form')  # Replace with the actual URL

    # Locate the first text field and enter a value
    text_field_1 = driver.find_element(By.ID, 'firstName')  # Replace with the actual locator
    text_field_1.clear()
    text_field_1.send_keys('RESHU')

    # Locate the second text field and enter a different value
    text_field_2 = driver.find_element(By.ID, 'lastName')  # Replace with the actual locator
    text_field_2.clear()
    text_field_2.send_keys('SHARMA')

    # Locate the third text field and enter another value
    text_field_3 = driver.find_element(By.ID, 'userEmail-wrapper')  # Replace with the actual locator

    text_field_3.send_keys('reshusharma123@gmail.com')

    # Optionally, you can submit the form if needed
    # For example, if there's a submit button:
    submit_button = driver.find_element(By.NAME, 'submitbutton')  # Replace with the actual locator
    submit_button.click()

    # Wait for a while to see the result (optional)
    time.sleep(5)

finally:
    # Close the WebDriver
    driver.quit()
