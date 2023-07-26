from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input[id='id_registration-email']")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "input[id='id_registration-password1']")
    REGISTRATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[id='id_registration-password2']")

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[id='id_login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[id='id_login-password']")

    SUBMIT_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')


class ProductPageLocators:
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    CART_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")


class CommonLocators:  # BasePageLocators
    CART_LINK = (By.CSS_SELECTOR, ".btn-group a")
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartLocators:
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    CART_ITEMS_DIV = (By.CLASS_NAME, "basket-items")

