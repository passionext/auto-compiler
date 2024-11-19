import random
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # A web browser without a graphical user interface, controlled programmatically.
    # Used for automation, testing, and other purposes.
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    website = input("Enter the website to autocompile: \nDO NOT CLOSE THE BLANK CHROME PAGE THAT HAS POPPED OUT!\n")
    page.goto(website)
    # Interact with login form. Using locator and xpath to autocompile the login form.
    page.locator('xpath=//*[@id="u"]').fill('') # Add the username for the login.
    page.locator('xpath=//*[@id="p"]').fill('') # Add the password for the login.
    page.get_by_role("button", name="Accedi").click() # Autoclick on the log-in button.
    #LOGGED
    # Autofill with normal information.
    page.locator('xpath=//*[@id="form"]/form/label[1]/input').fill('') # Username
    page.locator('xpath=//*[@id="form"]/form/label[2]/input').fill('') # Name
    page.locator('xpath=//*[@id="form"]/form/label[3]/input').fill('') # Age
    # When there is a drop-down menu, it is mandatory to use select_option
    page.locator('xpath=//*[@id="sesso"]').select_option('M') # Sex
    page.locator('xpath=//*[@id="funzione"]').select_option('') # Details
    page.locator('xpath=//*[@id="form"]/form/label[6]/input').fill('') # Email
    page.locator('xpath=//*[@id="form"]/form/label[7]/input').fill('') #Number

    # When there are possible multiple choice to select, you have to select the correspondent label[] position.
    page.locator('xpath=//*[@id="form"]/form/div[1]/label[4]/input').click()
    # There are 256 multiple choice questions. For add a bit of randomness, a list with the three possible choices
    # has been created. Then, through a FOR loop, all the questions are select one at a time and randomly answered with
    # an element from the created list. It's important that the list contains all the possible choices.
    choice = [1,2,3]
    # It's start from 2 because the first div element is filled before. Remember that range includes the first
    # element but excluded the last one; The range() function returns a sequence of numbers, starting from 0 by
    # default, and increments by 1 (by default), and stops before a specified number.
    for _ in range(2,258):
        page.locator(f'xpath=//*[@id="form"]/form/div[{_}]/input[{random.choice(choice)}]').click()
    page.pause()

