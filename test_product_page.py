import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize(
    "link",
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ],
)
def test_add_item_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket_btn()
    product_page.send_answer_alert()
    expected_name = product_page.get_product_name()
    expected_price = product_page.get_product_price()
    actual_name = product_page.get_product_name_in_basket()
    actual_price = product_page.get_product_price_in_basket()

    assert actual_name == expected_name, f"Expected {expected_name}, got {actual_name}"
    assert (
        actual_price == expected_price
    ), f"Expected {expected_price}, got {actual_price}"


@pytest.mark.xfail
def test_guest_cant_see_success_message_afted_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket_btn()
    product_page.should_be_message_about_success()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_message_about_success()


@pytest.mark.xfail
def test_message_diappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket_btn()
    product_page.should_be_message_of_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link_product)
    product_page.open()
    basket_page = product_page.go_to_basket()
    basket_page.should_be_empty_basket_text()
    basket_page.should_be_no_items_in_basket()
