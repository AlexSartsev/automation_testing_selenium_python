#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
	return str(int(x) + int(y))


try:
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	num1 = browser.find_element(By.ID, "num1")
	x = num1.text
	num2 = browser.find_element(By.ID, "num2")
	y = num2.text
	sum_x_y = calc(x, y)
	select = Select(browser.find_element(By.ID, "dropdown"))
	select.select_by_value(sum_x_y)

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
