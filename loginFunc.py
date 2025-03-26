from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Credentials
username = "standard_user"
password = "secret_sauce"

# Locate Elements
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# Input Username & Password
username_field.send_keys(username)
password_field.send_keys(password)

# Click Login Button
if login_button.is_enabled():  # Check if button is enabled before clicking
    login_button.click()
else:
    print("Login button is disabled!")

# Wait to see result
time.sleep(5)

# Verify Login Success (Checking for inventory page)
if "inventory" in driver.current_url:
    print("Login Successful!")
else:
    print("Login Failed!")

# Close Browser
driver.quit()
