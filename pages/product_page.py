from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()

    def should_be_add_message(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART_MESSAGE), "Added to cart message is not presented"

    def names_of_products_should_be_equal(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME) == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_ADDING_TO_BASKET), "Product name not a same!"

    def cart_cost_should_be_equal_price_of_the_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE) == self.browser.find_element(
            *ProductPageLocators.COST_BASKET), "Product price a not same!"
