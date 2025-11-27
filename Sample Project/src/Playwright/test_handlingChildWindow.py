
from playwright.sync_api import Page, expect

# Sample Playwright script to handle child windows
def test_childWindow(page:Page):
    page.goto("https://rahulshettyacademy.com/")

    with page.expect_popup() as newPage1:
        page.click('//a[text()="JOIN NOW"]')
        childPage1 = newPage1.value
        childPage1.wait_for_load_state()
        childPgTitle = childPage1.title()
        print(childPgTitle)