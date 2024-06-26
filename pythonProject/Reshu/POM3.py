import pytest
from selenium import webdriver
from login


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()  # You can specify the path to the ChromeDriver if needed
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password", [
    ("user1", "password1"),
    ("user2", "password2"),
])
def test_login(driver, username, password):
    driver.get("https://example.com/login")

    login_page = (driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    # Add assertions here to verify successful login
    assert "dashboard" in driver.current_url
