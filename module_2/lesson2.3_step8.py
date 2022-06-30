#explicit_wait

import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
# говорим Selenium проверять в течение 12 секунд, пока нужная цена = 100 не отобразится

button = browser.find_element(By.ID, 'book')
button.click()

x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

y = calc(x)

answer = browser.find_element(By.ID, 'answer').send_keys(y)
button_2 = browser.find_element(By.ID, 'solve')
button_2.click()



