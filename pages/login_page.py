from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login/" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert BasePage.is_element_present(*LoginPageLocators.LOGIN_FORM), "[There is no login form on the page]"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert BasePage.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "[There is no register form on the page]"
