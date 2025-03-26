import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Firefox()
# Credentials

driver.get('https://opensource-demo.orangehrmlive.com/')
#driver.maximize_window()
#driver.minimize_window()
driver.fullscreen_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header")

time.sleep(5)
driver.back();
driver.forward();
time.sleep(5)
driver.refresh();
driver.close()
