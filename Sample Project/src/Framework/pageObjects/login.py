from .dashboard import Dashboard


class LoginPage:

    def __init__(self,page):
        self.page = page   # Here self.page is a class variable, you can call anywhere within the class using 'self.' keyword

    def navigate(self):
         self.page.goto('https://rahulshettyacademy.com/client') 

    def login(self,userMailId, userPassword):
        self.page.locator('#userEmail').fill(userMailId)
        self.page.get_by_placeholder('enter your passsword').fill(userPassword)
        self.page.locator('#login').click()
        print(f'Logged in using {userMailId}')
        # Adding below line to avoid 2 line of code -> 1. Object creation and 2. Calling method using object
        # Below line serves the purpose of that "After login page is definitely moving to dashboard, so creating an object here and just calling this object in main Test file to avoid the extra line and increase more readablity"
        dashboardPage = Dashboard(self.page)
        return dashboardPage