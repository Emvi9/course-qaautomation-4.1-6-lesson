from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_alert_task_solved(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()


def test_do_product_names_match(browser):
    product_page = ProductPage(browser, link)
    assert product_page.do_product_names_match(), "[Added product name doesn't match with alert name]"


def test_do_product_prices_match(browser):
    product_page = ProductPage(browser, link)
    assert product_page.do_product_prices_match(), "[Cart total price doesn't math with this product price]"
