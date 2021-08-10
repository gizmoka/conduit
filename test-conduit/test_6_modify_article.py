from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from data import accepting_cookies, conduit_login, create_new_article, conduit_registration


def test_modify_article():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # Előfeltételek:
    accepting_cookies(browser)
    # conduit_registration(browser)
    conduit_login(browser)
    create_new_article(browser)

    # TC06: Meglévő blogpost szerkesztése
    edit_article_link = browser.find_element_by_css_selector("a[href='#/editor/new-title")
    edit_article_link.click()

    article_body_edited = browser.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
    article_body_edited.clear()
    article_body_edited.send_keys("New body comes here.")

    publish_article_button = browser.find_element_by_css_selector("button[type='submit']")
    publish_article_button.click()

    time.sleep(5)
    article_body_refilled = browser.find_element_by_css_selector('div[class="col-xs-12"] div p')
    assert article_body_refilled.text == "New body comes here."
    print("The article's body has been changed.")

    browser.quit()

