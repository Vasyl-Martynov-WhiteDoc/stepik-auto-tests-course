from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)
    # time.sleep(5)

    x_element = browser.find_element(By.ID,'input_value')
    x = x_element.text
    y = calc(x)
    answer_field = browser.find_element(By.ID,'answer')
    answer_field.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    time.sleep(5)
    submitBtn = browser.find_element(By.CLASS_NAME, 'btn')
    submitBtn.click()
    time.sleep(5)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
