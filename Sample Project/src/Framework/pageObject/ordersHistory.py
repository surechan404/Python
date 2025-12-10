class OrdersHistory:
    

    def __init__(self, page):
        self.page = page

    def ordersHistory(self):
        ordersHistoryUrl = self.page.url
        assert ordersHistoryUrl == 'https://rahulshettyacademy.com/client/#/dashboard/myorders'