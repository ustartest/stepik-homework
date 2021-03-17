# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects1.html"
num1 = "num1"
num2 = "num2"
answer = "answer"
checkbox = "robotCheckbox"
radiobutton = "robotsRule"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1_val = browser.find_element_by_id(num1)
    num2_val = browser.find_element_by_id(num2)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(int(num1_val.text)+int(num2_val.text)))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла