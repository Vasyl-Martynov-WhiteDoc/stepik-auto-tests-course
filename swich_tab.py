import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

try:
    journey_btn = browser.find_element(By.CLASS_NAME, 'btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.CSS_SELECTOR, 'label #input_value')
    x = x_element.text
    y = calc(x)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(y)
    button = browser.find_element(By.TAG_NAME,'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(5)
finally:
    browser.quit()