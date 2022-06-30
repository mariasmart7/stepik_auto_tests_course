import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    text = browser.find_element(By.ID, 'answer').send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
    radiobutton = browser.find_element(By.ID, 'robotsRule').click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

