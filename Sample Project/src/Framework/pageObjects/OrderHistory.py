import re
from time import sleep
from .orderDetails import OrderDetails

class OrderHistory:

    def __init__(self, page):
        self.page = page

    def viewOrder(self, orderID):
        row = self.page.locator('tr ').filter(has_text= orderID)
        print(orderID)
        row.get_by_role("button", name='View').click()
        orderDetailsPage = OrderDetails(self.page)
        return orderDetailsPage