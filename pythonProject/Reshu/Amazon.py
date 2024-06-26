from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# Initialize WebDriver (make sure ChromeDriver is in your PATH)
driver = webdriver.Chrome()

try:
    # Open Amazon homepage
    driver.get("https://www.amazon.com")

    # Wait until the search bar is present
    wait = WebDriverWait(driver, 10)
    search_bar = wait.until(expected_conditions.presence_of_element_located((By.ID, "twotabsearchtextbox")))

    # Search for "iPhone"
    search_bar.send_keys("iPhone")
    search_bar.send_keys(Keys.RETURN)

    # Wait until search results are loaded
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot")))

    # Select the first product in the search results
    first_product = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")[0]
    first_product.click()

    # Wait until the product page is loaded
    wait.until(expected_conditions.presence_of_element_located((By.ID, "productTitle")))

    # Add the product to the cart
    add_to_cart_button = wait.until(expected_conditions.element_to_be_clickable((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()

    # Handle any pop-up or additional offers (optional)
    try:
        no_thanks_button = wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".a-button-close.a-declarative")))
        no_thanks_button.click()
    except:
        pass

    # Verify item is added to cart (optional)
    wait.until(expected_conditions.presence_of_element_located((By.ID, "huc-v2-order-row-confirm-text")))
    print("Item added to cart successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)  # Just to see the result before closing, remove in actual script
    driver.quit()
