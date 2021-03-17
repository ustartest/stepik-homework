from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/registration1.html"
    # link = "http://suninjuly.github.io/registration2.html"
    value1 = "div.first_block>div.form-group.first_class>input.form-control.first"
    value2 = "div.first_block>div.form-group.second_class>input.form-control.second"
    value3 = "div.first_block>div.form-group.third_class>input.form-control.third"
    # value4 = "country"
    # value5 = "country"

    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(value3)
    input3.send_keys("IvanPetrov@gmail.com")
    # input4 = browser.find_element_by_id(value4)
    # input4.send_keys("Russia")
    # input5 = browser.find_element_by_id(value4)
    # input5.send_keys("Russia")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
