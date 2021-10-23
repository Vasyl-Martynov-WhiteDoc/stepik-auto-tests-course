import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)


try:
    first_name = browser.find_element(By.NAME, 'firstname').send_keys('Volodymyr')
    first_name = browser.find_element(By.NAME, 'lastname').send_keys('Melnyk')
    email = browser.find_element(By.NAME, 'email').send_keys('volodymyr.s.melnyk@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.NAME, 'file').send_keys(file_path)
    submitBtn = browser.find_element(By.CLASS_NAME, 'btn')
    submitBtn.click()
    time.sleep(10)
finally:
    browser.quit()