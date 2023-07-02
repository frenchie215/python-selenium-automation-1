from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC



PRODUCT_NAME = (By.CSS_SELECTOR, 'span#a-autoid-26.a-button.a-button-thumbnail.a-button-toggle')
COLOR_OPTIONS = (By.CSS_SELECTOR, 'span.selection')
CURRENT_COLOR = (By.CSS_SELECTOR, 'li#color_name_0')




@given('Open Amazon product B08FJC1CKR page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/MANGOPOP-Womens-Short-Sleeve-Shirt/dp/B08FJC1CKR/ref=sr_1_1?keywords=B08FJC1CKR&qid=1688334239&sr=8-1')



@when('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME)
    print(f'Current product: {context.product_name}')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['A Short Sleeve Black','B Long Sleeve White', 'B Long Sleeve Black']
    actual_colors = []

    colors = context.driver.find_element(*COLOR_OPTIONS) # =. [webelements1, webelement2, webelement 3]

    for color in colors[:3]:
        #webelement1
        color.click() #webelement1.click()
        current_color = context.driver.find_element(*CURRENT_COLOR)
        actual_colors += [current_color]

        assert expected_colors == actual_colors, \
        print f'Expected colors {expected_colors} did not match actual {actual_colors}'







