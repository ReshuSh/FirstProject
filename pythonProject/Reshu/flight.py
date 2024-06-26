from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# Initialize WebDriver (make sure WebDriver is in your PATH)
driver = webdriver.Chrome()

try:
    # Open Ixigo flight booking page
    driver.get("https://www.ixigo.com/flights")

    # Wait for the page to load and search for flights
    wait = WebDriverWait(driver, 10)

    # Enter departure city
    departure_city = wait.until(
        expected_conditions .presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter city or airport']")))
    departure_city.send_keys("New Delhi")
    time.sleep(2)

    # Enter arrival city
    arrival_city = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter city or airport']")
    arrival_city.send_keys("Mumbai")
    time.sleep(2)  # Wait for autocomplete to appear
    arrival_city.send_keys(Keys.ENTER)

    # Select departure date
    departure_date = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Departure']")
    departure_date.click()
    specific_date = wait.until(expected_conditions .element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='25 Jul 2024']")))
    specific_date.click()

    # Click on the search button
    search_button = driver.find_element(By.CSS_SELECTOR, "button.search-btn")
    search_button.click()

    # Wait for search results to load
    wait.until(expected_conditions .presence_of_element_located((By.CSS_SELECTOR, ".flight-listing")))

    # Select the first available flight
    first_flight = driver.find_elements(By.CSS_SELECTOR, ".flight-listing")[0]
    first_flight.click()

    # Wait for the booking page to load
    wait.until(expected_conditions .presence_of_element_located((By.CSS_SELECTOR, ".booking-form")))

    # Enter passenger details
    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='firstName']")
    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='lastName']")
    email = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
    mobile = driver.find_element(By.CSS_SELECTOR, "input[name='mobileNumber']")

    first_name.send_keys("John")
    last_name.send_keys("Doe")
    email.send_keys("john.doe@example.com")
    mobile.send_keys("9876543210")

    # Click on the continue button to proceed to payment
    continue_button = driver.find_element(By.CSS_SELECTOR, "button.book-flight-btn")
    continue_button.click()

    # Wait for the payment page to load
    wait.until(expected_conditions .presence_of_element_located((By.CSS_SELECTOR, ".payment-options")))

    # Print a success message (without completing the payment)
    print("Flight details entered successfully, ready for payment.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)  # Just to see the result before closing, remove in actual script
    driver.quit()
