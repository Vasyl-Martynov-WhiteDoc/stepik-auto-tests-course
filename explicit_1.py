from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
browser.implicitly_wait(5)
# browser.find_element_by_id("button")

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), ("$100"))
    )

button = browser.find_element(By.CLASS_NAME, "btn")
button.click()

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
y = calc(x)
answer_field = browser.find_element(By.ID, 'answer')
answer_field.send_keys(y)
time.sleep(2)
# submit_btn = browser.find_element(By.ID, 'solve' ).click
submit_btn = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'solve'))
    )
# browser.execute_script("return arguments[0].scrollIntoView(true);", submit_btn)
submit_btn.click()
time.sleep(10)

browser.quit()