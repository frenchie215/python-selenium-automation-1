from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep


#uppercase for locators)
AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.ID, 'nav-search-submit-button')
HAM_ICON = (By.ID, 'nav-hamburger-menu')
BEST_SELLER = (By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2']")
#HEADER_LINKS = (By.XPATH, "//div[@id='CardInstance_qQGa1UuSo-hWerLiCQD0w']")
#HEADER_LINKS = (By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[href='/Best-Sellers/zgbs/ref=zg_bsnr_tab'] a[href='/gp/new-releases/ref=zg_bsnr_tab'] a[href='/gp/movers-and-shakers/ref=zg_bsnr_tab'] a[href='/gp/most-wished-for/ref=zg_bsnr_tab'] a[href='/gp/most-gifted/ref=zg_bsnr_tab']")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Hamburger icon')
def click_search(context):
    context.driver.find_element(*HAM_ICON).click()


@when('Click on Best Sellers link')
def click_search(context):
    context.driver.find_element(*BEST_SELLER).click()


@then('Verify that header has 5 links')
def verify_header_link_count(context):
    header_link = context.driver.find_elements(*HEADER_LINKS)
    print(header_link)
    print('\nLink count: ', len(header_link))
    assert len(header_link) == 5, f'Expected 5 links, but got {len(header_link)}'