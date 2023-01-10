#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	link = "http://suninjuly.github.io/math.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)
	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(y)
	checkbox = browser.find_element(By.ID, "robotCheckbox")
	checkbox.click()
	radiobutton = browser.find_element(By.ID, "robotsRule")
	radiobutton.click()

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
