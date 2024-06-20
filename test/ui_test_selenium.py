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
text_box = wait.until(EC.presence_of_element_located((By.NAME, 'my-text')))
submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button')))

# 6. Take action on element
text_box.send_keys("Selenium")
submit_button.click()

#7. Request element information
message = driver.find_element(by=By.ID, value="message")
text = message.text

#8. End the session
driver.quit()



#####just to see changes