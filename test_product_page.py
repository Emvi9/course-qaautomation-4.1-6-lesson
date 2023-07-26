import time
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


@pytest.mark.need_review
class TestUserAddToCartFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = "Hardkj82kjabasskmjsdmbzhs"
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_cart(self, browser):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.press_add_to_cart()
        product_page.do_product_names_match(), f"[Name match error {self.link}]"
        product_page.do_product_prices_match(), f"[Price match error {self.link}"


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link(), "[There is no link on login page]"
    page.go_to_login_page(), "[Can't go to login page]"


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = CartPage(browser, product_page_link)
    page.open()
    page.go_to_cart()
    page.should_not_be_cart_items()
    page.should_be_empty_cart_message()
