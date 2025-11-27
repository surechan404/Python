from time import sleep
import playwright
from playwright.sync_api import Playwright,Page
from Utils.test_apiBase import Test_API_Utils

# This file is used to pass the items in local storage and bypass, certain functions or actions 
# to simulate the required scenario


def test_sessionStorage(playwright:Playwright, page:Page):
    apiUtilObj = Test_API_Utils()
    loginToken = apiUtilObj.test_login(playwright)
    print(f'Login Token = {loginToken}')

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Script to inject loginToken without logging in using UserId/Passwd in front-end
    # using """" to pass javascript code in python
    page.add_init_script(f"""localStorage.setItem('token',{loginToken})""")
    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_role('button',name='ORDERS').click()
    page.get_by_role('button',name='View').first.click()
    sleep(4)