from .base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        expected_url = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        actual_url = self.browser.current_url
        assert (
            actual_url == expected_url
        ), f"URL is wrong! Expected: {expected_url}, got: {actual_url}"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not present"

    def register_new_user(self, email, password):
        self.input_value(*LoginPageLocators.EMAIL_REGISTER, email)
        self.input_value(*LoginPageLocators.PASSWORD_REGISTER_1, password)
        self.input_value(*LoginPageLocators.PASSWORD_REGISTER_2, password)
        self.click_element(*LoginPageLocators.REGISTER_BTN)
