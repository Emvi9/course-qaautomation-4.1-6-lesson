from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.locators import CommonLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, find_by, selector):
        try:
            self.browser.find_element(find_by, selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, find_by, selector, timeout=4):  # Проверка на отсутствие элемента
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((find_by, selector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, find_by, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((find_by, selector)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        login_link = self.browser.find_element(*CommonLocators.LOGIN_LINK_INVALID)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*CommonLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_cart(self):
        self.browser.find_element(*CommonLocators.CART_LINK).click()
