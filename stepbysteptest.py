from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Step 1: Open Chrome Browser
driver = webdriver.Chrome()

# Step 2: Open Google
driver.get("https://www.google.com")

# Step 3: Locate the Search Box and Type Query
search_box = driver.find_element(By.NAME, "q")  # Find search bar
search_box.send_keys("Selenium Python")         # Type search text
search_box.send_keys(Keys.RETURN)               # Press Enter

# Step 4: Wait for Search Results to Load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
)

# Step 5: Click on the First Result
first_result = driver.find_element(By.CSS_SELECTOR, "h3")
first_result.click()

# Step 6: Wait for the New Page to Load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)

# Step 7: Print the Title of the Page
print("Page Title:", driver.title)

# Step 8: Close the Browser
driver.quit()
