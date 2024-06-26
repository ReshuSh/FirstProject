from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver using ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Navigate to the e-commerce website
    driver.get("https://www.example.com")  # Replace with the actual e-commerce site URL

    # Wait for the search bar to be present and enter "iPhone"
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search"))  # Adjust the locator as per the site's HTML
    )
    search_bar.send_keys("iPhone")
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load and display the products
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product"))  # Adjust the locator as per the site's HTML
    )

    # Click on the first product in the search results
    search_results[0].click()

    # Wait for the product page to load and the "Add to Cart" button to be clickable
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-button"))  # Adjust the locator as per the site's HTML
    )
    add_to_cart_button.click()

    # Optionally, wait for the confirmation message or navigate to the cart
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cart-icon"))  # Adjust the locator as per the site's HTML
    )
    cart_icon.click()

    # Print a message to indicate the script has successfully added the item to the cart
    print("iPhone has been added to the cart successfully.")

    # Optionally, wait and take a screenshot of the cart
    time.sleep(2)
    driver.save_screenshot('cart_screenshot.png')

finally:
    # Close the browser
    driver.quit()
