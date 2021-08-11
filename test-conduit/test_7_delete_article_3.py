from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import accepting_cookies, conduit_login, create_new_article, conduit_registration
import time


def test_delete_article():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # Előfeltételek:
    accepting_cookies(browser)
    time.sleep(2)
    conduit_login(browser)
    time.sleep(2)
    create_new_article(browser)

    # ~ ~ ~ ~ ~ TC-07: 1 BLOGPOSZT TÖRLÉSE ~ ~ ~ ~ ~ #
    delete_article_button = browser.find_element_by_css_selector('.btn.btn-outline-danger.btn-sm')
    time.sleep(2)
    delete_article_button.click()
    browser.refresh()
    time.sleep(7)

    # Asssert: az új url megváltozott
    url_after_deletion = "http://conduitapp.progmasters.hu:1667/#/articles/new-title"
    assert browser.current_url == url_after_deletion
    # print("Deleting this blogpost was a successful action. Congrats.")

    browser.quit()
