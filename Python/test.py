from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
web_element = driver.find_element(By.NAME, 'email')
web_element.send_keys('Damian' + Keys.ENTER)
time.sleep(30)
print(driver.title)
driver.quit()