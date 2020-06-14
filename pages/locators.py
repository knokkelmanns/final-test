from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span[class='btn-group'] a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG = (By.XPATH, "//*[@id='register_form']/button")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
