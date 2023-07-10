import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('link', ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail)
                                  ))
def test_guest_can_add_product_to_cart(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()
    assert product_page.do_product_names_match(), f"[Name match error {link}]"
    assert product_page.do_product_prices_match(), f"[Price match error {link}"

# def test_alert_task_solved(browser, link):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.press_add_to_cart()
#     product_page.solve_quiz_and_get_code()
#
#
# def test_do_product_names_match(browser, link):
#     product_page = ProductPage(browser, link)
#     assert product_page.do_product_names_match(), f"[Added product name doesn't match with alert name on{link}]"
#
#
# def test_do_product_prices_match(browser, link):
#     product_page = ProductPage(browser, link)
#     assert product_page.do_product_prices_match(), f"[Cart total price doesn't match with this product price on {link}]"
