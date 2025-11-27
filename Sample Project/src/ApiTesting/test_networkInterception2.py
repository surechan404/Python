from time import sleep
from playwright.sync_api import Page, expect, Route
 
 # This file simulates, When you're logged in as User A in Front-end and passing the URL to view order of User-B
 # by passing User B's order ID, Whether application is showing Authorization error or not.

 # Used method => route.continue_()



unauthURL = 'https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6927afed5008f6a9093cf70a'
# Order Id of user xomadi7495@okcdeals.com, Iamking@000

def networkInterceptor(route:Route):
    unauthResp = route.continue_(url=unauthURL)
    print(f'Unauthorized access Response : {unauthResp}')

def test_incorrectUserId(page:Page):
    page.goto('https://rahulshettyacademy.com/client')
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*', networkInterceptor)

    page.locator('#userEmail').fill('fepex31820@okcdeals.com')
    page.get_by_placeholder('enter your passsword').fill('Iamking@000')
    page.locator('#login').click()

    page.get_by_role('button',name='ORDERS').click()
    page.get_by_role('button',name='View').first.click()
    unauthErrMsg = page.locator('.blink_me').text_content()
    sleep(5)
    assert unauthErrMsg == 'You are not authorize to view this o'

    # print(f'Unauthorization error message in website is {unauthErrMsg}')