import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)  # Assertion

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
