from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


def calc(x):
  return str(abs(12*sin(x)))

browser = webdriver.Chrome()


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    a = browser.find_element(By.ID,'num1').text
    b = browser.find_element(By.ID,'num2').text
    c = calc()
    select = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
    select.select_by_value(c)
    submitBtn = browser.find_element(By.CLASS_NAME, 'btn')
    # submitBtn.wait.until(submitBtn.element_to_be_clickable((By.CLASS_NAME, 'btn')))
    submitBtn.click()
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
