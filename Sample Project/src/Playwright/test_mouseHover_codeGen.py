from time import sleep
from playwright.sync_api import Page, expect

# 1. Mouse Hover

def test_mouseHover(page:Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    page.locator('#mousehover').hover()
    sleep(3)
    page.get_by_role('link',name='Top').click()
    sleep(3)

# 2. CodeGen

# In terminal, enter "playwright codegen %URL%"
# Eg., "playwright codegen https://rahulshettyacademy.com/AutomationPractice/"
# This will open a browser window along with a codegen window.
