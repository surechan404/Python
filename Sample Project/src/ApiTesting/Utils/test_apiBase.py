import json
from math import e
from operator import contains
import playwright
from playwright.sync_api import Playwright, Page
from requests import head

class Test_API_Utils:

    def test_login(self, playwright:Playwright):
      # 1. Front-end Login Automation script:
        # browser = playwright.chromium.launch()
        # context = browser.new_context()
        # page = context.new_page()

        # page.goto('https://rahulshettyacademy.com/client')
        # page.locator('#userEmail').fill('rahulshetty@gmail.com')
        # page.locator('#userPassword').fill('Iamking@000')
        # login = page.locator('login').click()
        
      # 2. Back-end Login Automation script:  
        api_baseURL = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        loginPayload = {"userEmail":"fepex31820@okcdeals.com","userPassword":"Iamking@000"}
        
        loginResponse = api_baseURL.post('api/ecom/auth/login',
                         data=loginPayload)
        # assert loginResponse.ok
        loginResponseBody = loginResponse.json()
        # print(loginResponseBody)
        self.loginToken = loginResponseBody["token"]
        self.userId = loginResponseBody["userId"]
        # print(f'Token is {self.loginToken}')
        # print(f'User ID is {self.userId}')
        # prodCount = self.test_getProducts(playwright)
        # print(f'Product count before Purchase = {prodCount}')
        self.countBeforePurchase = 0
        return loginResponseBody["token"]

    
    # def test_getProducts(self, playwright:Playwright):
    #     productCountInCart = 0
    #     getProd = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
    #     getProdResponse = getProd.get(f'api/ecom/user/get-cart-count/{self.userId}').json()
    #     if(getProdResponse["count"] > 0):
    #         productCountInCart = getProdResponse["count"]
    #     print(f'Order count is {productCountInCart}')
    #     return productCountInCart

    # def test_getProdCountInCart(self, playwright:Playwright):
    #     getProd = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
    #     # print(f'User ID in getprodCountInCart {self.userId}')
    #     getProdCountResponse = getProd.get(f'/api/ecom/user/get-cart-count/{self.userId}',
    #                 headers={'Authorization': self.loginToken})
    #     self.getProdCountRespBody = getProdCountResponse.json()
    #     prodCount = self.getProdCountRespBody["message"] 
    #     if ('No Product in Cart' in prodCount):
    #         self.prodCount = 0 
    #     elif('Cart Data Found' in prodCount):
    #             self.prodCount = self.getProdCountRespBody["count"] 
    #     print(f'Product count in cart is {self.prodCount}')

    def test_createOrder(self, playwright:Playwright):
        BaseURL = 'https://rahulshettyacademy.com'
        self.test_login(playwright)
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

        # assert createOrderResponse.ok
        # self.test_getProdCountInCart(playwright)
        
        
        print('Exiting....')