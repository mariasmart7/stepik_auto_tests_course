from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, '[name=firstname]')
    first_name.send_keys('Maria')
    last_name = browser.find_element(By.CSS_SELECTOR, '[name=lastname]')
    last_name.send_keys('Smart')
    email = browser.find_element(By.CSS_SELECTOR, '[name = email]')
    email.send_keys('smart@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

