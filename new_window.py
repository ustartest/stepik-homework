# -*- coding: utf-8 -*-

from selenium import webdriver
import math
import time


link = "http://suninjuly.github.io/redirect_accept.html"
treasure = "input_value"
answer_loc = "answer"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.switch_to.window(window_name)
    # new_window = browser.window_handles[1]

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id(treasure)
    x = x_element.text
    answer_value = calc(x)

    input1 = browser.find_element_by_id(answer_loc)
    input1.send_keys(answer_value)

    button = browser.find_element_by_css_selector("button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
