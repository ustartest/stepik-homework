# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/execute_script.html"
treasure = "input_value"
answer = "answer"
checkbox = "robotCheckbox"
radiobutton = "robotsRule"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id(treasure)
    # x_element_value = x_element.get_attribute("valuex")
    x = x_element.text
    answer_value = calc(x)

    answer_field = browser.find_element_by_id(answer)
    answer_field.send_keys(answer_value)
    checkbox_el = browser.find_element_by_id(checkbox)
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox_el)
    checkbox_el.click()
    radiobutton_el = browser.find_element_by_id(radiobutton)
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_el)
    radiobutton_el.click()
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
#
# browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
