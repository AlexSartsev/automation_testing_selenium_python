#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = 'http://suninjuly.github.io/alert_accept.html'
	browser = webdriver.Chrome()
	browser.get(link)

	button_travel = browser.find_element(By.CSS_SELECTOR, 'div.container>button.btn')
	button_travel.click()
	confirm = browser.switch_to.alert
	confirm.accept()
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	result = calc(x)
	input = browser.find_element(By.ID, 'answer')
	input.send_keys(result)
	
	button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
	button.click()
	time.sleep(1)

finally:
	time.sleep(10)
	browser.quit()
