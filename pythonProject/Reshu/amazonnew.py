import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--incognito")  # Add this line to open browser in incognito mode
options.add_experimental_option("detach", True)

# Initialize the Chrome driver with options
driver = webdriver.Chrome(options=options)

# Maximize the browser window
driver.maximize_window()

driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=7473539534816465440&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9302611&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1")

# Wait for 3 seconds
time.sleep(3)

# Locate the search bar and enter "iphone"
search_bar = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
search_bar.send_keys("iphone")

# Wait for 3 seconds
time.sleep(3)

# Click on the search button
search_option = driver.find_element(By.ID, "nav-search-submit-button")
search_option.click()

# Wait for 3 seconds
time.sleep(3)

# Select the Samsung brand
brand = driver.find_element(By.LINK_TEXT, "Samsung")
brand.click()

# Wait for 3 seconds
time.sleep(3)

#Click on the first Samsung product
samsung_product = driver.find_element(By.XPATH, "(//span[@class='a-size-medium a-color-base a-text-normal'])[1]")
samsung_product.click()

# Wait for 3 seconds
time.sleep(3)

# Add the product to the cart
add_cart = driver.find_element(By.XPATH, "((//input[@name='submit.add-to-cart'])[2]")
add_cart.click()

# Wait for 3 seconds
time.sleep(3)
