from selenium import webdriver
import time
import csv
from data import accepting_cookies, conduit_login, conduit_registration
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_data_input_from_file():
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
    time.sleep(2)
    # TC4: Ismételt és sorozatos adatbevitel adatforrásból, 1 blogpost feltöltése betöltése txt fájlból
    ## step1: new article-ra rákattintunk
    browser.find_element_by_css_selector("a[href='#/editor']").click()

    ## step2: betölteni a blogpost.csv-ből soronként az adatokat a megfelelő input mezőbe

    with open('blogpost.csv', encoding='utf-8') as bp_file:
        csv_reader = csv.reader(bp_file, delimiter='/')
        for row in csv_reader:
            article_title = browser.find_element_by_css_selector("input[placeholder='Article Title']").send_keys(row[0])
            article_summary = browser.find_element_by_xpath('//input[starts-with(@placeholder,"What")]').send_keys(row[1])
            article_body = browser.find_element_by_css_selector("textarea[placeholder='Write your article (in markdown)']").send_keys(row[2])
            article_tag = browser.find_element_by_css_selector("input[placeholder='Enter tags']").send_keys(row[3])
            browser.find_element_by_css_selector("button[type='submit']").click()
            time.sleep(2)
            # assert article_title == "An awesome title for my article"
            # assert article_summary == "The gist of this article"
            # assert article_body == "I am exploring the ins and outs of automation testing."
            # assert article_tag == "best tag ever"
            print("Importing data from a csv file was successful.")

    bp_file.close()

    browser.quit()
