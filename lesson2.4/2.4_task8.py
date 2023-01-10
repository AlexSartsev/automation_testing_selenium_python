#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
	btn = browser.find_element(By.ID, "book")
	btn.click()

	# Решение уравнения
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	result = calc(x)

	# Ввод результата
	input = browser.find_element(By.ID, "answer")
	input.send_keys(result)

	# Нажатие на кнопку
	button = browser.find_element(By.ID, "solve")
	button.click()

finally:
	time.sleep(10)
	browser.quit()
