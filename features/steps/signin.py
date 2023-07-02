from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')


@given('Open Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')

@when('Click Orders')
def click_orders(context):
    context.driver.find_elements(By.ID, 'nav-orders').click()

@then('Verify Sign In page opens')
def verify_signin_opens(context):
    actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    assert actual_text == 'Sign in', f'Expected Sign in header but got {actual_text}'
    # verify email field present
    context.driver.find_element(*EMAIL)
    context.driver.wait.until(EC.url_contains('http://www.amazon.com/ap/signin'))
