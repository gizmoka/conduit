import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import accepting_cookies
import time

def test_cookies():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # ~ ~ ~ ~ ~ TC-02: COOKIES POLICY ELFOGADÁSA ~ ~ ~ ~ ~ #
    accepting_cookies(browser)
    time.sleep (2)

    # Assert: I accept! gomb nem található az oldalon
    with pytest.raises(NoSuchElementException):
        browser.find_element_by_xpath(
            '//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]')
        # print("Cookies policy buttons have disappeared from the homepage. So, I accept! button is working properly.")

    browser.quit()

