from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element(By.ID,'treasure')
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)
    answer_field = browser.find_element(By.ID,'answer')
    answer_field.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    time.sleep(1)
    submitBtn = browser.find_element(By.CLASS_NAME, 'btn')
    submitBtn.click()
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
