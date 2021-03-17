# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

treasure = "input_value"
answer_loc = "answer"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id(treasure)
x = x_element.text
answer_value = calc(x)

input1 = browser.find_element_by_id(answer_loc)
input1.send_keys(answer_value)

button = browser.find_element_by_id("solve")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
