from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_text(self):
        assert "Your basket is empty" in self.get_element_value(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket text is not presented, but should be"

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "Basket is not empty, items are present"
