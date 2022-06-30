from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1')
    num1_value = num1.text #получаем str
    num2 = browser.find_element(By.ID, 'num2')
    num2_value = num2.text #получаем str
    sum_value = int(num1_value) + int(num2_value)  #str переобразрвать в int для сложения чисел

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(sum_value))  #int перевести назад в str
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

