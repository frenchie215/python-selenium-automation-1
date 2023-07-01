from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')

@when('Click Orders')
def click_orders(context):
    context.driver.find_elements(By.ID, 'nav-orders').click()

@then('Verify Sign In page opens')
def signin_result(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[@cclass='a-spacing-small']").text
    assert expected_result == actual_text, f'Expected {expected_result} but got actual {actual_text}'