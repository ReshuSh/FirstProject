# pages/login_page.py
from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME_FIELD = (By.ID, "username")  # Replace with the actual locator of the username field
    PASSWORD_FIELD = (By.ID, "password")  # Replace with the actual locator of the password field
    LOGIN_BUTTON = (By.ID, "loginBtn")    # Replace with the actual locator of the login button

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        self.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
