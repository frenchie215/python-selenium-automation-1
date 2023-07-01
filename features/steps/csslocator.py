from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(executable_path='/Users/francesgibson/Desktop/Automation/chromedriver')


# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

#by CSS, using ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')

#By CSS, using class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-lop')
#you can always omit tag => .icp-nav-flag-lop
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-lop')
#multiple classes =>
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-lop.icp-nav-flag-us.icp-nav-flag')

#By CSS, using attributes (except ID and Class)
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
# multiple attributes
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/bestsellers/?ref_=nav_cs_bestsellers'][tabindex='0']")

#class + attribute # put classes in front
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers'][tabindex='0']")

# attributes, partial match *= (means contains)
driver.find_element(By.CSS_SELECTOR, "a[href*='?ref_=nav_cs_bestsellers']")

