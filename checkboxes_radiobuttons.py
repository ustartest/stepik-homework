# -*- coding: utf-8 -*-


from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"
value1 = "input_value"
answer = "answer"
checkbox = "robotCheckbox"
radiobutton = "robotsRule"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id(value1)
    x = x_element.text
    answer_value = calc(x)

    answer_field = browser.find_element_by_id(answer)
    answer_field.send_keys(answer_value)
    checkbox_el = browser.find_element_by_id(checkbox)
    checkbox_el.click()
    radiobutton_el = browser.find_element_by_id(radiobutton)
    radiobutton_el.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла