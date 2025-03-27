import time

from selenium import webdriver

viewports = [(1024, 786), (786, 1024), (375, 367), (455, 896)]

driver = webdriver.Chrome()
driver.get('https://www.google.co.uk/')


try:
    for width,height in viewports:
        driver.set_window_size(width, height)
        time.sleep(5)

finally:
    driver.close()