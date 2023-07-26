import time

# from selenium.webdriver.common.by import By  # to delete

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
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "[There is no login form on the page]"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), \
            "[There is no register form on the page]"

    def register_new_user(self, email, password):
        reg_form_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_form_pass = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        reg_from_pass_repeat = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT)
        submit_btn = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)

        reg_form_email.click()
        reg_form_email.send_keys(email)

        reg_form_pass.click()
        reg_form_pass.send_keys(password)

        reg_from_pass_repeat.click()
        reg_from_pass_repeat.send_keys(password)

        submit_btn.click()
