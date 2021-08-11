from selenium import webdriver
import time
import csv
from data import accepting_cookies, conduit_login, conduit_registration
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_data_input_from_file():
    browser_options = Options()
    browser_options.headless = False
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # Előfeltételek
    accepting_cookies(browser)
    time.sleep(7)
    conduit_login(browser)
    time.sleep(2)

    # ~ ~ ~ ~ ~ TC-10: 1 BLOGPOSZT FELTÖLTÉSE FÁJLBÓL ~ ~ ~ ~ ~ #

    ## Step1: a 'new article'-ra rákattintunk
    browser.find_element_by_css_selector("a[href='#/editor']").click()

    ## Step2: betöltjük a fájból soronként az adatokat a megfelelő input mezőbe

    with open('blogpost.csv', encoding='utf-8') as bp_file:
        csv_reader = csv.reader(bp_file, delimiter='/')
        for row in csv_reader:
            article_title = browser.find_element_by_css_selector("input[placeholder='Article Title']")
            article_summary = browser.find_element_by_xpath('//input[starts-with(@placeholder,"What")]')
            article_body = browser.find_element_by_css_selector(
                "textarea[placeholder='Write your article (in markdown)']")
            article_tag = browser.find_element_by_css_selector("input[placeholder='Enter tags']")

            article_title.send_keys(row[0])
            article_summary.send_keys(row[1])
            article_body.send_keys(row[2])
            article_tag.send_keys(row[3])

            publish_article_button = browser.find_element_by_css_selector('button[type="submit"]')
            publish_article_button.click()

            # Assert: blogpost feltöltésre került, megjelenik
            article_body_new = browser.find_element_by_css_selector("div[class='col-xs-12'] div p")
            assert article_body_new.text == row[2]
            # print("Importing data from a csv file was successful.")

    bp_file.close()

    browser.quit()
