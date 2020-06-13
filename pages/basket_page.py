from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def basket_empty(self):
        assert self.is_not_element_present(*BasketLocators.ITEMS_TO_BUY_NOW), "There are items in the basket"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketLocators.MESSAGE_EMPTY_BASKET), "No message that basket is empty"
