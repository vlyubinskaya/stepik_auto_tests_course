from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x, y):
    return str(x + y)

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    x_element = x_element.text
    x = int(x_element)
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    y_element = y_element.text
    y = int(y_element)

    result = calc(x, y)
    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(result)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

except Exception as e:
    raise e

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
