"""import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_open_url(browser):
    browser.get("https://www.lambdatest.com/")


def test_login(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/")
    browser.find_element_by_id("txtUsername").send_keys("Admin")
    browser.find_element_by_id("txtPassword").send_keys("admin123")
    browser.find_element_by_id("btnLogin").click()

    title = browser.title

    assert title == 'OrangeHRM'


def test_letras_mus(browser):
    browser .get('https://www.letras.mus.br/')

    # find and click in an icon then return to the previous page
    element = browser.find_element_by_css_selector('a[data-slug="rock"]')
    element.click()
    browser.back()

    # find the search field and submit 'Tim Maia' keyword
    search_element = browser.find_element_by_id('main_suggest')
    search_element.send_keys('Tim Maia')
    search_element.send_keys(Keys.RETURN)

    # os anuncios ficam encapsulados pelos iframes
    # para que o browser aponte para o iframe eh necessario chama-lo
    time.sleep(10)
    browser.switch_to.frame('master-1')
    # print do primeiro link dos anuncios
    link_elements = browser.find_elements_by_tag_name('a')
    print(link_elements[0].get_attribute('href'))
    pass


def test_phptravel(browser):
    browser.get('https://www.phptravels.net/offers')

    price_classes = browser.find_elements_by_class_name(name="price")
    price_list = []
    for price in price_classes:
        price_list.append(price.text)

    clean_price_list = []
    for price in price_list:
        if price.startswith('$'):
            price_number = price[1:]
            price_integer = int(price_number.replace(',', ''))
            clean_price_list.append(price_integer)
    print(sorted(clean_price_list))
    pass


def test_cart(browser):
    url = 'http://automationpractice.com/index.php'
    browser.get(url)

    expect_total = 0
    # find all product containers avaiable
    product_containers = browser.find_elements_by_class_name('product-container')
    # for each of them, add to cart
    for product_container in product_containers:
        # scroll to product_container
        scroll = browser.execute_script("arguments[0].scrollIntoView();", product_container)
        try:
            # hover over product container
            hover = ActionChains(driver)
            hover.move_to_element(product_container)
            hover.perform()
            time.sleep(1)
            # add-to-cart is child of product-container
            add_to_cart = product_container.find_element_by_css_selector('a[title="Add to cart"]')
            add_to_cart.click()
            time.sleep(5)  # waiting confirmation modal open

            continue_shopping = browser.find_element_by_css_selector('span[title="Continue shopping"')
            continue_shopping.click()  # closing modal confirmation to continue shopping
            time.sleep(2)  # time to gatantee modal is closed

            expect_total += 1  # validation quantity of products in the cart
            product_name = product_container.find_element_by_class_name('product-name')
            print(product_name.get_attribute('textContent'))  # print product label
        except:
            pass

    shopping_cart = browser.find_element_by_class_name('shopping_cart')
    quantity = shopping_cart.find_element_by_css_selector('span.ajax_cart_quantity:nth-child(2)')

    cart_total = quantity.get_attribute("textContent")
    containers_total = str(expect_total)

    assert cart_total == containers_total"""