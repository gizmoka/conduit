from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_homepage():
    browser_options = Options()
    browser_options.headless = True
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
    URL = "http://conduitapp.progmasters.hu:1667/#/"
    browser.get(URL)
    browser.implicitly_wait(10)

    # TC0: Homepage megfelelően töltődött be
    h1_element = browser.find_element_by_tag_name("h1")
    assert h1_element.text == "conduit"
    print('We are happy. The homepage has appeared.')
    browser.quit()
