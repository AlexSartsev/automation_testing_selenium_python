#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	result = calc(x)

	input = browser.find_element(By.ID, "answer")
	browser.execute_script("return arguments[0].scrollIntoView(true);", input)
	input.send_keys(result)
	check_box = browser.find_element(By.ID, "robotCheckbox")
	check_box.click()
	radio_button = browser.find_element(By.ID, "robotsRule")
	radio_button.click()

	# Отправляем заполненную форму
	button = browser.find_element(By.CSS_SELECTOR, "button.btn")
	button.click()

	# Проверяем, что смогли зарегестрироваться
	# ждем загрузки страницы
	time.sleep(1)

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()
