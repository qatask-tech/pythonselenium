from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Set up WebDriver (Ensure ChromeDriver is installed)
driver = webdriver.Chrome()

# Step 2: Open Google
driver.get("https://www.google.com")

# Step 3: Locate Search Box and Enter Query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)

# Step 4: Click on the First Result
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
first_result.click()

# Wait for the page to load
time.sleep(3)

# Step 5: Print Page Title
print("Page Title:", driver.title)

# Step 6: Close Browser
driver.quit()
