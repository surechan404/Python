from time import sleep
from playwright.sync_api import Playwright, Page, expect
from Utils.test_apiBase import Test_API_Utils

def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

# API calls from test_api_base.py file
    apiUtils = Test_API_Utils()
    orderId = apiUtils.test_createOrder(playwright)
    print(f'Order Id is{orderId}')

# Web calls
    page.goto('https://rahulshettyacademy.com/client')
    page.locator('#userEmail').fill('fepex31820@okcdeals.com')
    page.get_by_placeholder('enter your passsword').fill('Iamking@000')
    page.locator('#login').click()

    page.get_by_role('button',name='  ORDERS').click()
    # for index in range(page.locator('th').count()):
    #     page.locator('t')
    page.locator('th').filter(has_text=orderId)
    print('Order is present in the UI')    
    sleep(3)