from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/cats.html?"
browser.get(link)
browser.implicitly_wait(5)
# browser.find_element_by_id("button")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

browser.quit()