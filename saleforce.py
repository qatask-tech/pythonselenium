from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Setup WebDriver

from selenium.webdriver.firefox.service import Service

service = Service(r"C:\WebDriver\geckodriver.exe")

driver = webdriver.Firefox(service=service)


# Step 2: Open Website
driver.get("https://computing-saas-6788--yasirsandb.sandbox.my.site.com/spring/s/")

# Step 3: Fill out the form using SelectorHub locators
driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("John Doe")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("john.doe@example.com")

# Step 4: Click a checkbox (Example)
driver.find_element(By.XPATH, "//input[@type='radio'][@value='$1,000 - $2,000']").click()

# Step 5: Submit the form
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

# Step 6: Close browser
time.sleep(3)
driver.quit()
