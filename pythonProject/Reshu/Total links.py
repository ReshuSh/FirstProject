from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# Set up the WebDriver (use the path where you have installed the ChromeDriver)
driver = webdriver.Chrome()

# Open Amazon
driver.get('https://www.amazon.com')

# Search for iPhone
search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
search_box.send_keys('iPhone')
search_box.send_keys(Keys.RETURN)

try:
    # Wait for search results to load and display the results
    wait = WebDriverWait(driver, 10)
    results = wait.until(expected_conditions .presence_of_all_elements_located((By.CSS_SELECTOR, 'div.s-main-slot div.s-result-item')))

    # Click on the first result
    results[0].find_element(By.CSS_SELECTOR, 'h2 a').click()

    # Wait for the product page to load
    wait.until(expected_conditions .presence_of_element_located((By.ID, 'add-to-cart-button')))

    # Add to cart
    add_to_cart_button = driver.find_element(By.ID, 'add-to-cart-button')
    add_to_cart_button.click()

    # Wait for the cart overlay to appear and close it
    wait.until(expected_conditions .presence_of_element_located((By.ID, 'attach-close_sideSheet-link')))
    close_cart_overlay_button = driver.find_element(By.ID, 'attach-close_sideSheet-link')
    close_cart_overlay_button.click()

    # Go to cart
    driver.find_element(By.ID, 'nav-cart').click()

    # Proceed to checkout
    wait.until(expected_conditions .presence_of_element_located((By.NAME, 'proceedToRetailCheckout')))
    proceed_to_checkout_button = driver.find_element(By.NAME, 'proceedToRetailCheckout')
    proceed_to_checkout_button.click()

    # Wait until checkout page loads (This will stop before the payment page for safety)
    wait.until(expected_conditions .presence_of_element_located((By.CSS_SELECTOR, 'div.a-box-group.a-spacing-base')))

    # Print a message indicating that the script has reached the final stage before payment
    print("Reached the final stage before payment. Please review and place the order manually.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the WebDriver
    time.sleep(5)
    driver.quit()
