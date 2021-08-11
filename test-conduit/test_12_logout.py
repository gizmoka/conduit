import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import accepting_cookies, conduit_login, conduit_registration


def test_logout():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # Előfeltételek
    accepting_cookies(browser)
    conduit_login(browser)
    time.sleep(2)

    # ~ ~ ~ ~ ~ TC-11: KIJELENTKEZÉS ~ ~ ~ ~ ~ #
    logout_link = browser.find_element_by_xpath("//a[@active-class='active']")
    logout_link.click()

    # Assert: a logout gomb már nem található az oldalon
    with pytest.raises(NoSuchElementException):
        browser.find_element_by_xpath("//a[@active-class='active']")
    # print("Log out link is no more available. So, you have succesfully logged out from this website.\nHave a nice day! ")

    browser.quit()
