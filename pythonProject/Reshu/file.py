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

    # Locate the text field using its name, id, class, etc.
    text_field = driver.find_element(By.ID, 'reshu')



    # Clear the text field if needed
    text_field.clear()

    # Enter the desired value into the text field
    text_field.send_keys('reshu')


    # Optionally, you can submit the form if needed
    text_field.send_keys(Keys.RETURN)

    # Wait for a while to see the result (optional)
    time.sleep(5)

finally:
    # Close the WebDriver
    driver.quit()
