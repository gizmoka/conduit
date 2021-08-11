import time
from selenium import webdriver
from data import accepting_cookies, conduit_login, conduit_registration
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_pagination():
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

    # ~ ~ ~ ~ ~ LAPOZÁS (GLOBAL FEED-EN) ~ ~ ~ ~ ~ #
    pagination_page_1 = browser.find_element_by_xpath("//a[normalize-space()='1']")
    time.sleep(2)
    pagination_page_1.click()

    # Assert: új lapozóoldalra érkezve az 1. blogpost body-ja megváltozott
    new_page_article_body = browser.find_element_by_xpath("//h1[normalize-space()='Mi eget mauris pharetra et']")
    assert new_page_article_body.text == "Mi eget mauris pharetra et"
    # print("Hurray, you have done it!")

    browser.quit()
