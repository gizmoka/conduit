from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from data import *

URL = "http://conduitapp.progmasters.hu:1667/#/"
def test_add_new_article():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    browser.get(URL)
    browser.implicitly_wait(10)

    # Előfeltételek:
    accepting_cookies(browser)
    # conduit_registration(browser)
    conduit_login(browser)
    time.sleep(2)

    # TC6: 1 blogpost létrehozása

    # Elnavigálunk a 'new article' oldalra
    new_article_link = browser.find_element_by_css_selector("a[href='#/editor']")
    new_article_link.click()

    # 1 'new article' létrehozása
    article_title_input = browser.find_element_by_css_selector("input[placeholder='Article Title']")
    article_about_input = browser.find_element_by_xpath('//input[starts-with(@placeholder,"What")]')
    write_article_textarea = browser.find_element_by_css_selector(
        ("textarea[placeholder='Write your article (in markdown)']"))
    tags_input = browser.find_element_by_css_selector("input[placeholder='Enter tags']")

    article_title_input.send_keys("New Title")
    article_about_input.send_keys("Great summary")
    write_article_textarea.send_keys(
        "Yar Pirate Ipsum. Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm.")
    tags_input.send_keys("lorem_tag")

    publish_article_button = browser.find_element_by_css_selector("button[type='submit']")
    publish_article_button.click()

    # assert: megjelent-e az új article body része az oldalon
    published_article = browser.find_element_by_css_selector("p")
    assert published_article.text == "Yar Pirate Ipsum. Prow scuttle parrel provost Sail ho shrouds spirits boom mizzenmast yardarm."
    print("New published article has been found on this site. So, adding new article functin works fine.")
    browser.quit()

