import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser=browser, url=link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
    homepage_link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = CartPage(browser, homepage_link)
    page.open()
    page.go_to_cart()
    page.should_not_be_cart_items()
    page.should_be_empty_cart_message()
