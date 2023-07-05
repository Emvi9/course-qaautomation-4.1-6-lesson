from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input[id='id_registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input[id='id_registration-password1']")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[id='id_registration-password2']")

    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[id='id_login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[id='id_login-password']")
