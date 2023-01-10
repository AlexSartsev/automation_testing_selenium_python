#!/usr/bin/python

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Получаем путь к файлу

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'file.txt'
file_path = os.path.join(current_dir, file_name)

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	input_name = browser.find_element(By.XPATH, "//input[@name='firstname']")
	input_name.send_keys('Ivan')
	input_surname = browser.find_element(By.XPATH, "//input[@name='lastname']")
	input_surname.send_keys('Ivanov')
	input_email = browser.find_element(By.XPATH, "//input[@name='email']")
	input_email.send_keys('ivan89ivanov@mail.com')
	file = browser.find_element(By.ID, "file")
	file.send_keys(file_path)

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
