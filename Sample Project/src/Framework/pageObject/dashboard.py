from pageObject.ordersHistory import OrdersHistory


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def ordersNavLinkClick(self):
        self.page.get_by_role('button',name='ORDERS').click()
        ordHistory = OrdersHistory(self.page)
        return(ordHistory)