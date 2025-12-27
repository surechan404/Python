from typing import Self
import pytest
import json
from playwright.sync_api import Playwright
from pageObjects.login import LoginPage
from utils.test_apiBase_fw import Test_API_Utils_fw

# #Json file -> util->access into test.
with open('data/testData.json') as f:
    test_data = json.load(f)
    print(test_data)

# getting user credentials list from json file to iterate each user values on eby one 
user_credentials_list = test_data['userCredentials'] 


# passing Json data as test case and passing it into userCred parameter
@pytest.mark.parametrize('user_credentials' ,user_credentials_list)  # using "user_credentials_list" data to 'user_credentials' variable/fixture to iterate the the values and creating a fixture using a same name as well
def test_e2e_web_api(playwright:Playwright, user_credentials, browserInstance):
    # Start tracing
    
# API calls from test_api_base.py file
    apiUtils = Test_API_Utils_fw()
    orderId = apiUtils.test_createOrder(playwright, user_credentials)
    # print(f'Order Id is{orderId}')

# Mail Id and Password from test_data.json
    mailId = user_credentials['userMailId']
    password = user_credentials['userPassword']
    
# 1. Login page
    loginPage = LoginPage(browserInstance) # login is the object of LoginPage class
    loginPage.navigate()

# 2. Dashboard page
    dashboardPage = loginPage.login(mailId, password)
    orderHistoryPage = dashboardPage.selectOrderNavLink() 
    
# 3. OrderHistory page
    orderDetailsPage = orderHistoryPage.viewOrder(orderId)
     
# 4. OrderDetails page    
    orderDetailsPage.verifyOrderMessage()
    
    
# Notes:
# 1. Above test methods/class include @pytest.mark.smoke/someName to run specific tests
# 2. In terminal we can run using "pytest -m smoke or -m someName" to run specific tests
# 3. Similarly we can exclude specific tests using "pytest -m 'not smoke'" to exclude smoke tests
# 4. To run specific tests based on keyword in terminal we can use "pytest -k 'keywordName'" to include tests
# 5. To exclude specific tests based on keyword in terminal we can use "pytest -k 'not keywordName'" to exclude tests
# 6. To run tests in parallel:
     # a. Install pytest-xdist using "pip install pytest-xdist" in terminal
        # Eg. pytest test_website_fw.py -n 3  --> This will run tests in 3 parallel threads 
# 7. To generate HTML report use below command in terminal:
     # a. To install pytest-html plugin use "pip install pytest-html" in terminal
     # a. pytest test_website_fw.py --browser_name chrome -n 3 --html=reports/report.html        
# 8. To generate Allure report use below command in terminal:
        # a. To install allure-pytest plugin use "pip install allure-pytest
        # b. pytest test_website_fw.py --browser_name chrome -n 3 --alluredir=allure-results
        # c. allure serve allure-results
# 9. To take screenshots, enter --tracing on in terminal while running tests
        # Eg. pytest test_website_fw.py --browser_name chrome -n 3 --tracing on
        # --tracing can be equals to 'on', 'off', 'retain-on-failure'
    ##### SCREENSHOTS ARE NOT WORKING AS EXPECTED IN PARALLEL EXECUTION - NEED TO CHECK #####
    ##### test-reports FOLDER IS NOT GETTING CREATED FOR HTML REPORT - NEED TO CHECK #####
    # Reason for test-reports folder not getting created is because of wrong command used in terminal
        # Correct command to get screenshots is:
        # pytest test_website_fw.py --browser_name chrome -n 3 --trace on --html=reports/report.html