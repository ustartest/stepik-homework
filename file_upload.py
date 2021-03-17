# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os


link = "http://suninjuly.github.io/file_input.html"
firstname_loc = 'input[name="firstname"]'
lastname_loc = 'input[name="lastname"]'
email_loc = 'input[name="email"]'
file_loc = "file"

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector(firstname_loc)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(lastname_loc)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(email_loc)
    input3.send_keys("IvanPetrov@gmail.com")
    file_input = browser.find_element_by_id(file_loc)
    file_input.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
