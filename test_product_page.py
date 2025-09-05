import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from helper import generate_registration_data


class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_add_to_basket_btn()
        product_page.send_answer_alert()
        product_page.should_be_correct_product_added_to_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_afted_adding_product_to_basket(
        self, browser
    ):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_add_to_basket_btn()
        product_page.should_be_message_about_success()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_message_about_success()

    @pytest.mark.xfail
    def test_message_diappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.click_add_to_basket_btn()
        product_page.should_be_message_of_is_disappeared()


class TestGuestOnProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        product_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.go_to_login_page()


class TestGuestBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        product_link = (
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        )
        product_page = ProductPage(browser, product_link)
        product_page.open()
        basket_page = product_page.go_to_basket()
        basket_page.should_be_empty_basket_text()
        basket_page.should_be_no_items_in_basket()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        email, password = generate_registration_data()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_link = (
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        )
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.should_be_message_about_success()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_link = (
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        )
        product_page = ProductPage(browser, product_link)
        product_page.open()
        product_page.click_add_to_basket_btn()
        product_page.should_be_correct_product_added_to_basket()
