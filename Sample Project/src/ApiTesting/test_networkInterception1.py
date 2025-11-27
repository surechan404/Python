from time import sleep
from playwright.sync_api import Page, expect

# expectedPayload is used as a sample response from server, which is used to render the webpage according to the response.
# Through this we can reduce  waiting time to perform data clearing or reproduce a specific scenario..

# Used method => page.route() and route.fulfill()

expectedPayload = {"data":[],"message":"No Orders"}
def networkInterceptor(route):
    route.fulfill(json = expectedPayload)



def test_noOrderPresent(page:Page):
    page.goto('https://rahulshettyacademy.com/client')
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*', networkInterceptor)
    page.locator('#userEmail').fill('fepex31820@okcdeals.com')
    page.get_by_placeholder('enter your passsword').fill('Iamking@000')
    page.locator('#login').click()

    page.get_by_role('button',name='ORDERS').click()
    noOrderText = page.locator('.mt-4').text_content()
    print(f'Text of Order page is {noOrderText}')
    sleep(4)