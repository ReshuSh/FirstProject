from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the webdriver
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH or specify the path to chromedriver

# Open the initial URL
driver.get("https://example.com")

# Store the ID of the original window
original_window = driver.current_window_handle

# Open a new window by executing JavaScript
driver.execute_script("window.open('https://www.google.com', '_blank');")

# Wait for the new window to open
time.sleep(2)

# Get a list of all open windows
windows = driver.window_handles

# Switch to the new window (assuming it's the second window)
for window in windows:
    if window != original_window:
        driver.switch_to.window(window)
        break

# Perform any actions on the new window
driver.find_element(By.NAME, 'q').send_keys('Selenium' + Keys.RETURN)

# Wait for a bit to see the results
time.sleep(2)

# Switch back to the original window
driver.switch_to.window(original_window)

# Perform any actions on the original window
# For example, we can print the current URL
print(driver.current_url)

# Close the driver
driver.quit()
