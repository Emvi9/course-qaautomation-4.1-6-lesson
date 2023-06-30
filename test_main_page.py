from pages.main_page import MainPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser=browser, url="http://selenium1py.pythonanywhere.com/")
    page.open()
    page.go_to_login_page()
