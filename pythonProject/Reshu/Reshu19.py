
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://www.blazedemo.com/login")
# find_element:--> it's a method which we can use when we need to get one element from single locator

driver.find_element(By.ID, "email").send_keys("TEST")
driver.find_element(By.ID, "password").send_keys("TEST")
ls = driver.find_elements(By.CLASS_NAME,"form-control")
print(len(ls))
for x in ls:
    x.clear()
    x.send_keys("TEST")
    x.clear()

    if x .get_attribute("id") == "email":
        x.send_keys("JAY KRISHNA")
    if x.get_attribute("id") == "password":
        x.send_keys("RADHA@@^$@$&")
