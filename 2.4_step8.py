from selenium import webdriver
import time
import os 
import math
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    browser1 = WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # нажимаем на кнопку
    button = browser.find_element(By.ID, "book").click()

    # считать значение переменной х
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    # вычислить значение y
    y = calc(x)

    # вывести значение вычисленной функции
    y1=browser.find_element(By.ID, 'answer').send_keys(y)
    #y1.send_keys(y)
   
    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    # закрываем браузер после всех манипуляций
    browser.quit()