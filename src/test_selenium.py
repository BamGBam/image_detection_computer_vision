from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "/home/bgoshtasbi/Desktop/Selenium"
# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 1. Navigate to your page
driver.get('http://localhost:5000')

# 2. Find the file input element
file_input = driver.find_element(By.ID, 'fileInput')

# 3. Upload the file
file_input.send_keys('/path/to/your/file')

# 4. Click the upload button 
upload_button = driver.find_element(By.XPATH, '//button[normalize-space()="Upload"]')
upload_button.click()

# 5. Wait for the result to appear
wait = WebDriverWait(driver, 10)  # Increase the timeout if necessary
result = wait.until(EC.presence_of_element_located((By.ID, 'result')))

# 6. Verify the result or you can use the result however you see fit
print(result.text)

driver.quit()