from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ✅ Provide the correct path to ChromeDriver
chromedriver_path = "C:\\WebDriver\\chromedriver.exe"

# ✅ Set up ChromeDriver service
service = Service(chromedriver_path)

# ✅ Configure Chrome options
options = Options()
options.add_argument("--start-maximized")  # Open in full screen
options.add_argument("--disable-popup-blocking")  # Ensure popups are not blocked

# ✅ Initialize WebDriver
try:
    driver = webdriver.Chrome(service=service, options=options)
    print("✅ Browser opened successfully!")

    # Open the website
    driver.get("http://bms.afi-usa.com/shop/")
    time.sleep(5)  # Wait for the page to load

    # ✅ Check for and close the popup (if present)
    try:
        popup_close_button = driver.find_element(By.ID, "title-Close dialog")
        popup_close_button.click()
        print("✅ Popup closed successfully!")
    except:
        print("⚠ No popup found, proceeding...")

    # ✅ Click the Account button to open the login modal
    try:
        account_button = driver.find_element(By.XPATH, "//a[@data-bs-toggle='modal' and @data-bs-target='#sign-in-modal']")
        account_button.click()
        print("✅ Account button clicked successfully!")
        time.sleep(3)  # Wait for modal to open
    except Exception as e:
        print(f"❌ Account button click failed: {e}")

    # ✅ Enter login details
    try:
        email_input = driver.find_element(By.NAME, "Email")
        password_input = driver.find_element(By.NAME, "Password")

        email_input.send_keys("techleadz.cfm@gmail.com")
        password_input.send_keys("12345678")

        print("✅ Email and Password entered successfully!")

        # ✅ Click the Sign In button
        login_button = driver.find_element(By.ID, "loginFormSubmitId")
        login_button.click()
        print("✅ Sign In button clicked successfully!")

    except Exception as e:
        print(f"❌ Error in login process: {e}")

    time.sleep(5)  # Wait for login to complete
    driver.quit()
    print("🚪 Browser closed.")

except Exception as e:
    print(f"❌ Error occurred: {e}")
