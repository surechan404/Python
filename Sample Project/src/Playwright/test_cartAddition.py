from time import sleep
from playwright.sync_api import sync_playwright,Page,expect

# 1. Sample PLaywright script to perform add to cart and validate
def test_UI_Validations1(page:Page):
    page.goto("https://rahulshettyacademy.com/angularpractice/shop")
    
    note8 = page.locator("app-card").filter(has_text="Samsung Note 8")
    note8.get_by_role('button').click()   

    nokiaEdge = page.locator("app-card").filter(has_text="Nokia")
    nokiaEdge.get_by_role('button').click()   
    sleep(5)

    page.get_by_text("Checkout").click()
    sleep(5)

    cart = page.locator(".media-body")
    expect(cart).to_have_count(2)











