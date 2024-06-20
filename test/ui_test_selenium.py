from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1- Starting the session
driver = webdriver.Chrome()

# 2- Take action on browser
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.get("http://127.0.0.1:5500/proj1_classification/src/index.html")

time.sleep(5)
# 3- Request browser information
title = driver.title

# 4. Establish Waiting Strategy
driver.implicitly_wait(0.5)

# # 5. Find an element
# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# 5. Find an element with explicit wait
wait = WebDriverWait(driver, 10)  # wait for up to 10 seconds

# Replace `my-text` with the ID of the file input, which is `fileInput`
file_input = wait.until(EC.presence_of_element_located((By.ID, 'fileInput')))
# The button doesn't have a name or an id, in this case use tag name
upload_button = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'button')))

# 6. Take action on element
# file_input.send_keys("<path_to_the_file_you_want_to_upload>")
upload_button.click()

#7. Request element information
result = driver.find_element(by=By.ID, value="result")
text = result.text

#8. End the session
driver.quit()