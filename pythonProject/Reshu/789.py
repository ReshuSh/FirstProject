from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Path to the ChromeDriver executable
CHROMEDRIVER_PATH = 'path/to/chromedriver'

# URL of the webpage with the dropdown
URL = 'https://google.com'

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get(URL)

    # Wait for the dropdown to be present in the DOM and visible
    dropdown_element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "id_of_dropdown"))
    )

    # Create a Select object
    dropdown = Select(dropdown_element)

    # Select an option by visible text
    dropdown.select_by_visible_text("Option Text")

    # Select an option by value
    dropdown.select_by_value("option_value")

    # Select an option by index (e.g., the second option, index starts at 0)
    dropdown.select_by_index(1)

    # You can add more interactions with the dropdown here as needed

finally:
    # Close the browser
    driver.quit()
