from curses.textpad import Textbox
from time import sleep
from playwright.sync_api import sync_playwright,Page,expect

    # 1. Textbox handling
def test_moreValidations(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    expect(page.get_by_placeholder("Hide/Show Example"))
    Textbox = page.get_by_placeholder("Hide/Show Example")
    Textbox.fill("Test Input")
    page.get_by_role('button',name="Hide").click()
    expect(Textbox).not_to_be_visible()

    # 2. Alert handing
    # page.get_by_placeholder('Enter Your Name').filter(name='enter-name')
def test_alertHandling(page:Page):
     page.goto("https://rahulshettyacademy.com/AutomationPractice/")
     sleep(2)
     page.on("dialog", lambda dialog:dialog.accept())  # Not understood this properly
     page.get_by_role('button',name='Confirm').click()

    # 3. Frame Handling
def test_frameHandling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageFrame = page.frame_locator('#courses-iframe')
    pageFrame.get_by_role('link',name='browse learning path').click()
    sleep(5)








    # # Checkbox validation
    # checkbox = page.locator("#checkBoxOption1")
    # checkbox.check()
    # expect(checkbox).to_be_checked()
    # checkbox.uncheck()
    # expect(checkbox).not_to_be_checked()
    
    # # Static dropdown validation
    # dropdown = page.locator("select#dropdown-class-example")
    # dropdown.select_option("option2")
    # selected_option = dropdown.input_value()
    # assert selected_option == "option2"
    
    # # Dynamic dropdown validation
    # page.locator("#autocomplete").fill("ind")
    # sleep(2)  # Wait for suggestions to load
    # suggestions = page.locator(".ui-menu-item div")
    # count = suggestions.count()
    # for i in range(count):
    #     if suggestions.nth(i).inner_text() == "India":
    #         suggestions.nth(i).click()
    #         break
    # selected_value = page.locator("#autocomplete").input_value()
    # assert selected_value == "India"
    
    # # Visibility toggle validation
    # text_box = page.locator("#displayed-text")
    # expect(text_box).to_be_visible()
    # page.locator("#hide-textbox").click()
    # expect(text_box).not_to_be_visible()
    # page.locator("#show-textbox").click()
    # expect(text_box).to_be_visible()