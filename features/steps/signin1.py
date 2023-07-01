from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service


service = Service('/Users/francesgibson/Desktop/Automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//span[text()='& Orders']").click()

expected_result = 'Sign In'
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
print(actual_result)