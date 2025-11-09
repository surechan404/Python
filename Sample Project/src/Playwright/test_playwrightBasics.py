# 0. Exceute commands on OS's terminal
# 1. Install Python 
# 2. Install pytest => pip install pytest
# 3. Install pytest-playwright => pip install pytest-playwright 
# 4. Install test engines and browsers for playwright => playwright install
import playwright
from playwright.sync_api import Page, Playwright, sync_playwright, expect
from time import sleep

def test_pwBasic(playwright):
    browser = playwright.chromium.launch(headless=False)
# 5. context refers to a independant separate browser window
    context1 = browser.new_context()
    page = context1.new_page()
    page.goto("https://www.google.com")


# 6. page fixture should be used only when Chromium and Headless mode, Single context is required,
# not for big project or customized test execution

# 7. If you want to run specific method, Go to execution directory,
# a) pytest ..filename.py::method name
# b) pytest ..filename.py::method name--headed => For Headed mode

def test_pwShortcut(page:Page):
    page.goto("https://www.rahulshettyacademy.com")

# 8. Chromium

def test_chromium(page: Page, playwright:Playwright):
    page.goto("https://www.google.com")
    page.get_by_role("combobox").fill("Playwright")
    page.get_by_role("combobox").press("Enter")
    expect(page.get_by_label("I'm not a robot")).to_be_visible()

# 9. Firefox
    
def test_fireFox(page:Page, playwright:Playwright):
    firefoxBrowser = playwright.firefox.launch()
    context = firefoxBrowser.new_context()
    page = context.new_page()

    page.goto(("https://www.google.com"))
    page.get_by_role("combobox").fill("Playwright")
    page.get_by_role("combobox").press("Enter")
    expect(page.get_by_label("I'm not a robot")).to_be_visible()

    # sleep(5000)
    # page.context.close()
