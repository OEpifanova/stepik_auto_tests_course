from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    # нажимаем на кнопку
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    # перейти на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # считать значение переменной х
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text

    # вычислить значение y
    y = calc(x)

    # вывести значение вычисленной функции
    y1=browser.find_element(By.ID, 'answer').send_keys(y)
    #y1.send_keys(y)
   
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()