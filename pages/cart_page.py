from pages.base_page import BasePage
from pages.locators import CartLocators


class CartPage(BasePage):
    def should_not_be_cart_items(self):
        assert self.is_not_element_present(*CartLocators.CART_ITEMS_DIV), "[Cart is not empty]"

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartLocators.EMPTY_CART_MESSAGE), "[No message about empty cart]"
