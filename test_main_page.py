import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


main_url = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, main_url)
        main_page.open()
        main_page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser, main_url)
        main_page.open()
        main_page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        main_page = MainPage(browser, main_url)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestGuestBasketFromMainPage:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        main_page = MainPage(browser, main_url)
        main_page.open()
        basket_page = main_page.go_to_basket()
        basket_page.should_be_empty_basket_text()
        basket_page.should_be_no_items_in_basket()
