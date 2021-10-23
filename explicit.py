from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/wait2.html"
browser.get(link)
browser.implicitly_wait(5)
# browser.find_element_by_id("button")

button = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text

browser.quit()