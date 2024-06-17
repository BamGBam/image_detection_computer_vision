from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# specify path to chromedriver if it's not on the system PATH
# webdriver_service = Service('/home/Desktop/Selenium/chrome-linux64')
# img = cv2.imread("/home/bgoshtasbi/Desktop/ML Project/proj1_classification/image_4.jpg")

webdriver_service = Service('/chrome-linux64')
driver = webdriver.Chrome(service=webdriver_service)

driver.get('http://www.google.com/')

print(driver.title)  # prints the title of the page

driver.quit()