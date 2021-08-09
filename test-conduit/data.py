import time

def accepting_cookies(browser):
    accept_cookies_button = browser.find_element_by_xpath("//button[@class='cookie__bar__buttons__button cookie__bar__buttons__button--accept']")
    accept_cookies_button.click()

def conduit_registration(browser):
    browser.find_element_by_xpath('//a[@href="#/register"]').click()
    username_input = browser.find_element_by_xpath('//input[@placeholder="Username"]')
    email_input = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    password_input = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    username_input.send_keys("GumiBogyo")
    email_input.send_keys("gumibogyo@gmail.com")
    password_input.send_keys("GumiBogyo01")
    time.sleep(7)
    browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.pull-xs-right').click()

def conduit_login(browser):
    browser.find_element_by_xpath('//a[normalize-space()="Sign in"]').click()
    email_input = browser.find_element_by_css_selector('input[placeholder="Email"]')
    password_input = browser.find_element_by_css_selector('input[placeholder="Password"]')
    email_input.send_keys("gumibogyo@gmail.com")
    password_input.send_keys("GumiBogyo01")
    time.sleep(6)
    button = browser.find_element_by_css_selector('button.btn.btn-lg.btn-primary.pull-xs-right')
    browser.execute_script('arguments[0].click()', button)

def create_new_article(browser):
    # elnavigálunk a 'new article' oldalra
    browser.find_element_by_css_selector("a[href='#/editor']").click()

    # 'new article' létrehozása
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

def conduit_logout(browser):
    logout_button = browser.find_element_by_xpath("//a[@active-class='active'] and [@class='nav-link']")
    logout_button.click()

