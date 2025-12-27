import pytest

@pytest.fixture(scope="session")
def user_credentials(request):  # Here 'request' is a param to get the global variable
    return request.param 

# addoption is user to get the runtime parameter from command line and use it in code
# Eg. browser name, headless true/false etc 

# 1. Browser
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chromium", help="Enter browser name.."    
        )
# 2. Base URL
# parser.addoption(
#         "--base_url", action="store", default="https://rahulshettyacademy.com", help="Enter base URL.."    
#         )   


@pytest.fixture
def browserInstance(playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
          browser = playwright.chromium.launch(headless=False)
    elif browser_name == 'firefox':
         browser = playwright.firefox.launch(headless=False)
    elif browser_name == 'safari':
         browser = playwright.webkit.launch(headless=False)
    else: print('Unsupported browser name..')     


    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()  
