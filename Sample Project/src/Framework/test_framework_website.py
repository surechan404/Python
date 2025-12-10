import json
from time import sleep
from playwright.sync_api import Playwright, Page, expect
import test
# from Framework.pageObject import dashboard, ordersHistory
from pageObject.login import LoginPage
from pageObject.dashboard import DashboardPage
from utils.test_apiBase_fw import Test_API_Utils
import pytest
 
# Test data file - JSON format
with open('data/testData.json') as file:
    testData = json.load(file)
    # print(testData)  
    userCredentialsList = testData['userCredentials']
    baseURL = testData['baseURL']

# @pytest.mark.parametrize('userCred', userCredentialsList, baseURL)
@pytest.mark.parametrize('userCred, baseURL', [(cred, baseURL) for cred in userCredentialsList])

def test_e2e_web_api(playwright:Playwright, browserInitiate,  userCred, baseURL ):
    userMailId = userCred['userMailId']
    userPassword = userCred['userPassword']

# API calls from test_api_base.py file
    apiUtils = Test_API_Utils()
    orderId = apiUtils.test_createOrder(playwright, userCred, baseURL)

# Web calls - Login > Orders View
    login = LoginPage(browserInitiate)
    login.navigate(browserInitiate)
    dashboard = login.login(browserInitiate, userMailId, userPassword)
    orderHist = dashboard.ordersNavLinkClick()
    orderHist.ordersHistory()
