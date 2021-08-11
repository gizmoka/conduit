import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import accepting_cookies, conduit_login, conduit_logout

def test_login():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # Előfeltételek
    accepting_cookies(browser)

    # ~ ~ ~ ~ ~ TC-04: BELÉPÉS ~ ~ ~ ~ ~ #
    time.sleep(5)
    sign_in_button = browser.find_element_by_xpath("//a[@href='#/login']")
    time.sleep(2)
    sign_in_button.click()
    email_input = browser.find_element_by_css_selector('input[placeholder="Email"]')
    password_input = browser.find_element_by_css_selector('input[placeholder="Password"]')
    email_input.send_keys("gumibogyo@gmail.com")
    password_input.send_keys("GumiBogyo01")
    login_button = browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.pull-xs-right')
    time.sleep(2)
    login_button.click()
    time.sleep(6)

    # Assert: username megjelenik-e a menubaron
    username_input = browser.find_element_by_xpath('//a[normalize-space()="GumiBogyo"]')
    assert username_input.text == "GumiBogyo"
    # print("Conclusion: The login proccess is done properly.")

    browser.quit()