from selenium.webdriver.common.by import By
from behave import when, then

CART = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=sw_gtc')


@then('Verify cart has {expected_count} item(s)')
def verify_search_result(context, expected_count):
    actual_text = context.driver.find_element(*CART).text
    assert expected_count == actual_text, f'Expected {expected_count} but got actual {actual_text}'