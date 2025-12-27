
from .OrderHistory import OrderHistory


class Dashboard:

    def __init__(self, page):
        self.page = page

    def selectOrderNavLink(self):
        self.page.get_by_role('button',name='ORDERS').click()
        orderHistoryPage = OrderHistory(self.page)    
        return orderHistoryPage