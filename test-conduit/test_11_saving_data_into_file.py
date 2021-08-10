from selenium import webdriver
import time
from data import accepting_cookies, conduit_login, conduit_registration
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def test_lementes_feluletrol():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # Előfeltételek
    accepting_cookies(browser)
    # conduit_registration(browser)
    conduit_login(browser)

    # TC08: Adatok listázása, blogpostok listázása

    # a saját blogpostokat megkeresem
    ## step1: username-re rákattintunk a menübaron
    browser.find_element_by_xpath('//div[@class="container"]//ul/li[4]/a').click()
    time.sleep(5)

    ## step2: Favorited Articles-re kattintok, utána My Articles-re (csak így működik)
    browser.find_element_by_css_selector("a[href='#/@GumiBogyo/favorites']").click()
    browser.find_element_by_css_selector("a[href='#/@GumiBogyo/']").click()
    time.sleep(6)
    my_article_title_text = browser.find_element_by_css_selector("h1").text
    my_article_body_text = browser.find_element_by_xpath("//a[@class = 'preview-link']/p").text

    time.sleep(2)
    with open("one_of_my_articles.txt", "w", encoding='utf-8') as my_art:
        my_art.write(my_article_title_text + "\n" + my_article_body_text + "\n")
        # my_art.write(my_article_title_text)
        # my_art.write(my_article_body_text)

    my_art.close()

    # assert: a csv fájl nem üres
    if os.stat("one_of_my_articles.txt").st_size == 0:
        print('empty')


    browser.quit()