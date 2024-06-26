from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get("https://blazedemo.com/login")
# print total links of webpage
link = driver.find_elements(By.TAG_NAME,"a")
print("total links", len(link))
for links in link:
    print(links.text)
    print(links.get_attribute("href"))

# print total button of webpage
button = driver.find_elements(By.TAG_NAME,"button")
print("total button : ", len(button))
# print total textfield of webpage
textfield = driver.find_elements(By.TAG_NAME,"input")
print("total textfield: ", len(textfield))
# print total frame of webpage
frame = driver.find_elements(By.TAG_NAME, "iframe")
print("total frames :", len(frame))
# print total span of webpage
span = driver.find_elements(By.TAG_NAME,"span")
print("total span :", len(span))
# print total div of webpage
div = driver.find_elements(By.TAG_NAME,"div")
print("total div ", len(div))
for divs in div:
    print(divs.get_attribute("id"))