from urllib import request
from playwright.sync_api import Playwright
import pytest

# 1. request is a global fixture like playwright
# 2. It is used to access local test variable


# addOption(parser) is used to define the browser for execution either default or multiple options

def addoption(parser):
      parser.addoption(
            "--browser", action='store', default='chrome', help='Browser selection'
      )

@pytest.fixture(scope='session')
def userCredentials(request):
      return request.param

# User need to input as below in terminal,
# pytest test_framework_website.py --browser firefox/chromium/webkit --headed
# Here --browser is the argument to get the browser name from terminal

@pytest.fixture(scope='session')
def browserInitiate(playwright:Playwright, request):
    # browser = playwright.chromium.launch(headless=False)
      browserName = request.config.getoption('browser')
      if browserName == 'chromium':
            browser = playwright.chromium.launch()
      elif browserName == 'firefox':
            browser = playwright.firefox.launch()
      elif browserName == 'safari':
            browser = playwright.webkit.launch()
      else:
         print('Invalid browser name..')                      
      
      context = browser.new_context()
      page = context.new_page()
      yield page
    # page.close()
      context.close()
      browser.close()