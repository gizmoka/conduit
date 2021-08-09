from selenium import webdriver
from data import accepting_cookies
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_cookies():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # TC02: Cookies policy elfogadása
    accepting_cookies(browser)

    # Nem maradt megnyomható gomb az oldalon, miután elfogadtuk a cookies policy-t, erre assertezni
    assert browser.find_elements_by_xpath("//button") == []
    print("Cookies policy buttons have disappeared from the homepage. So, I accept! button is working properly.")
    browser.quit()

