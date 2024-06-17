from selenium import webdriver
import time


# Specify the path to chromedriver if it's not on the system PATH.
# webdriver_service = webdriver.chrome.service.Service('/Desktop/Selenium')
# driver = webdriver.Chrome(service=webdriver_service)
driver = webdriver.Chrome()
# Open the local file in the browser
# driver.get('file:///path/to/your/index.html')
# /home/bgoshtasbi/Desktop/ML Project/proj1_classification/src/index.html
driver.get('file:///home/bgoshtasbi/Desktop/ML Project/proj1_classification/src/index.html')
# Simulate uploading a file
from selenium.webdriver.common.by import By

upload = driver.find_element(By.ID, "fileInput")  # type: ignore
upload.send_keys("/path/to/your/test/file.jpg")

# Click the upload button
driver.find_element_by_css_selector("button").click()  # type: ignore

# Add a delay to ensure the image gets uploaded and results are rendered
time.sleep(5) 

# Check the results
result = driver.find_element_by_id("result").text  # type: ignore
print(result)

driver.quit()