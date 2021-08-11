import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from datetime import datetime, timezone
from data import accepting_cookies

def test_registration():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # Előfeltételek
    accepting_cookies(browser)

    # ~ ~ ~ ~ ~ TC-03: REGISZTRÁCIÓ ~ ~ ~ ~ ~ #
    register_button = browser.find_element_by_xpath('//a[@href="#/register"]')
    time.sleep(2)
    register_button.click()

    username_input = browser.find_element_by_xpath('//input[@placeholder="Username"]')
    email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')

    # minden regisztráláskor új adatok generálása
    dynamic_variable = str(datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"))
    dynamic_email = dynamic_variable + "@gmail.com"
    username_input.send_keys(dynamic_variable)
    email_input.send_keys(dynamic_email)
    password_input.send_keys("Adminka01,")

    sending_data = browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.pull-xs-right')
    sending_data.click()
    time.sleep(3)

    # Assert: sikeres regisztráció üzenet
    successful_registration_message = browser.find_element_by_css_selector('div.swal-text').text
    assert successful_registration_message == "Your registration was successful!"
    browser.find_element_by_xpath("//button[normalize-space()='OK']").click()
    # print("Congrats! Your registration has been successful.")

    browser.quit()