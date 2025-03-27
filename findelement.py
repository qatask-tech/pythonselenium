from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Find search box using its name attribute and enter text
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")

# Submit the search form
search_box.submit()

# Close browser
driver.quit()
