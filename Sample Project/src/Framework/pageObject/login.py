from pageObject.dashboard import DashboardPage


class LoginPage:
     def __init__(self,page):
          self.page = page

          
     def navigate(self,page):
          baseUrl = "https://rahulshettyacademy.com/client"
          self.page.goto(baseUrl)

     def login(self, page, mailId, password):
          page.locator('#userEmail').fill(mailId)
          page.get_by_placeholder('enter your passsword').fill(password)
          page.locator('#login').click()
          dashboard = DashboardPage(page)        
          return dashboard