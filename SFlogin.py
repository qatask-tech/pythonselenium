from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 🔹 Salesforce Staging Login Details
LOGIN_URL = "https://computing-saas-6788--yasirsandb.sandbox.my.salesforce.com"
USERNAME = "spencer@afi-usa.com.yasirsandb"  # ✅ Corrected string format
PASSWORD = "5m!GuC33;]Yd=yn1"  # ✅ Corrected closing quote

# 🔹 Initialize the WebDriver (Ensure you have the correct path for 'chromedriver')
driver = webdriver.Chrome()

# 🔹 Open Salesforce Login Page
driver.get(LOGIN_URL)
driver.maximize_window()

# 🔹 Wait for the username field to appear
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))  # ✅ More reliable

# 🔹 Enter Username
username_field.send_keys(USERNAME)

# 🔹 Wait and enter Password
password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
password_field.send_keys(PASSWORD)

# 🔹 Click Login Button
login_button = wait.until(EC.element_to_be_clickable((By.ID, "Login")))
login_button.click()

# 🔹 Wait for login success
wait.until(EC.url_contains("home"))

# 🔹 Verify login success
if "home" in driver.current_url:
    print("✅ Login Successful!")
else:
    print("❌ Login Failed!")

# 🔹 Close the Browser
driver.quit()
