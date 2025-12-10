from email.mime import base
import json
from math import e
from operator import contains
import playwright
from playwright.sync_api import Playwright, Page
import pytest
from requests import head

class Test_API_Utils:

    
    def test_login(self, playwright:Playwright, userCred, baseURL):
        userMailId = userCred['userMailId']
        userPassword = userCred['userPassword']
      # Back-end Login Automation script:  
        api_baseURL = playwright.request.new_context(base_url= baseURL)
        loginPayload = {"userEmail":userMailId ,"userPassword": userPassword}
        
        loginResponse = api_baseURL.post('api/ecom/auth/login',
                         data=loginPayload)
        # assert loginResponse.ok
        loginResponseBody = loginResponse.json()
        # print(loginResponseBody)
        self.loginToken = loginResponseBody["token"]
        self.userId = loginResponseBody["userId"]
        # print(f'Product count before Purchase = {prodCount}')
        self.countBeforePurchase = 0
        return loginResponseBody["token"]

    def test_createOrder(self, playwright:Playwright, userCred, baseURL):
        BaseURL = baseURL
        self.test_login(playwright, userCred, baseURL)
        orderPayload ={"_id":"69246f685008f6a909377d5a","product":{"_id":"68a961959320a140fe1ca57e","productName":"iphone 13 pro","productCategory":"electronics","productSubCategory":"mobiles","productPrice":55000,"productDescription":"Apple phone","productImage":"https://rahulshettyacademy.com/api/ecom/uploads/productImage_1650649561326.jpg","productRating":"0","productTotalOrders":"0","productStatus":True,"productFor":"women","productAddedBy":"admin","__v":0}}
        order_context = playwright.request.new_context(base_url=BaseURL)
        createOrderResponse =  order_context.post('/api/ecom/user/add-to-cart',
                            data=orderPayload,
                            headers = {'Authorization': self.loginToken})
        createOrderRespBody = createOrderResponse.json()
        
        placeOrder = playwright.request.new_context(base_url=BaseURL)
        placeOrderPayload = {"orders":[{"country":"India","productOrderedId":"68a961959320a140fe1ca57e"}]}
        placeOrderResp = placeOrder.post(url='api/ecom/order/create-order',
                        data=placeOrderPayload,
                        headers={'Authorization' : self.loginToken})
        placeOrderRespBody = placeOrderResp.json()
        print(f"Place Order Response Body is .. {placeOrderRespBody}")
        
        item1 = placeOrderRespBody['orders'][0]
        return item1