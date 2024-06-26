import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Ensure chromedriver is in PATH

    def test_search_in_google(self):
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title)

        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("Selenium")
        elem.send_keys(Keys.RETURN)

        self.assertIn("Selenium", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

