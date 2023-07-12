import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage

# @pytest.mark.parametrize('link', ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param(
#                                       "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                       marks=pytest.mark.xfail)
#                                   ))
# def test_guest_can_add_product_to_cart(browser, link):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.press_add_to_cart()
#     product_page.solve_quiz_and_get_code()
#     assert product_page.do_product_names_match(), f"[Name match error {link}]"
#     assert product_page.do_product_prices_match(), f"[Price match error {link}"

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

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.press_add_to_cart()
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.press_add_to_cart()
#     page.success_message_should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = CartPage(browser, product_page_link)
    page.open()
    page.go_to_cart()
    page.should_not_be_cart_items()
    page.should_be_empty_cart_message()
