from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
print("Browser Launched")
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# driver.get("https://google.com")
driver.get("https://help.testim.io/docs/api-access")
print("Website Loaded")
title = driver.title
print("Title of the page is:", title)
driver.implicitly_wait(0.5)
time.sleep(5)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
print("Elements Located")

text = text_box.text
print("Text extracted:", text)
time.sleep(5)

driver.quit()
print("Browser Closed")