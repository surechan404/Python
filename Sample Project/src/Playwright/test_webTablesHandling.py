from playwright.sync_api import Page,expect

# Handling dynamic Web tables

def test_webTables(page:Page):
    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')
     
    for index in range(page.locator('th').count()):
          if page.locator("th").nth(index).filter(has_text='Price').count()>0:
               priceColValue = index
               print(f"Price is in column no. {index}")
               break
    riceRow = page.locator("tr", has_text="Rice" )
    priceValue = (riceRow.locator("td").nth(priceColValue))
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")