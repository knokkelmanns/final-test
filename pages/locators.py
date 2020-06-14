from selenium.webdriver.common.by import By


class BasePageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "span[class='btn-group'] a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators:
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")


class LoginPageLocators:
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG = (By.XPATH, "//*[@id='register_form']/button")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
