import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path='drivers/chromedriver')
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path='drivers/geckodriver')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

def test_open_url(browser):
    browser.get("https://www.lambdatest.com/")


def test_login(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/")
    browser.find_element_by_id("txtUsername").send_keys("Admin")
    browser.find_element_by_id("txtPassword").send_keys("admin123")
    browser.find_element_by_id("btnLogin").click()

    title = browser.title

    assert title == 'OrangeHRM'


def test_basic_duckduckgo_search(browser):
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'

    browser.get(URL)

    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(PHRASE + Keys.RETURN)

    link_divs = browser.find_elements_by_css_selector('#links > div')
    assert len(link_divs) > 0

    xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == PHRASE