from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    # Wait for the "I'm Feeling Lucky" button to be clickable
    lucky_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "btnI"))
    )

    # Click using JavaScript
    driver.execute_script("arguments[0].click();", lucky_button)

    # Switch to the new tab or page
    WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])

    # Wait for the new page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    print("Successfully navigated!")

except Exception as e:
    print("Error occurred:", str(e))

finally:
    driver.quit()
