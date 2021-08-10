from selenium import webdriver
import time
from data import conduit_login, accepting_cookies, conduit_registration
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_list_data():
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

    # kigyűjtjük a saját blogpostok body-jait (bodies) és kiírjuk egy articles_list.txt-be
    article_preview_bodies = browser.find_elements_by_xpath("//div[@class='article-preview']/a/p")

    articles_list = []
    for article in article_preview_bodies:
        articles_list.append(article.text + '\n')

    with open('articles_list.txt', 'a', encoding='utf-8') as artlist:
        for element in articles_list:
            artlist.write(element)
    artlist.close()

    # assert: a saját blogposztjaim darabszámának ellenőrzése
    all_articles_titles = browser.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div/div/div/a/h1')
    assert len(all_articles_titles) == len(articles_list)
    print(f"Saját blogposztok darabszáma: {len(articles_list)}")

    browser.quit()
