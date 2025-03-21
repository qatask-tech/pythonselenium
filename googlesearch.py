from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Open Chrome Browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find search box by NAME and enter text
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium WebDriver")
search_box.send_keys(Keys.RETURN)  # Press ENTER

# Wait for results to load
time.sleep(3)

# Get first search result by CSS_SELECTOR and click it
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
first_result.click()

# Print the title of the page
print("Page Title:", driver.title)

# Close the browser
driver.quit()
