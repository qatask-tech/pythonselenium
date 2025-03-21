from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Locate Search Box using XPath
search_box = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")

# Type in Search Box
search_box.send_keys("Selenium Python")

# Close the Browser
driver.quit()
