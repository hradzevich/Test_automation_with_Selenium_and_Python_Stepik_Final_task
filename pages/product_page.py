from .base_page import BasePage
from locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_btn(self):
        self.click_element(*ProductPageLocators.ADD_BTN)

    def get_product_name(self):
        self.get_element_value(*ProductPageLocators.PRODUCT_NAME)

    def get_product_price(self):
        self.get_element_value(*ProductPageLocators.PRODUCT_PRICE)

    def send_answer_alert(self):
        self.solve_quiz_and_get_code()

    def should_be_view_basket_btn(self):
        self.is_element_present(*ProductPageLocators.VIEW_BASKET_BTN)

    def get_product_name_in_basket(self):
        self.get_element_value(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)

    def get_product_price_in_basket(self):
        self.get_element_value(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).replace(
            "£", ""
        ).strip()

    def should_be_message_about_success(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_be_message_of_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Element is not desappeared"
