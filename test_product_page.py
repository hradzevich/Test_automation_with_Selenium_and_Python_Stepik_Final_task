from pages.product_page import ProductPage


def test_add_item_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_backet_btn()
    product_page.send_answer_alert()
    expected_name = product_page.get_product_name()
    expected_price = product_page.get_product_price()
    actual_name = product_page.get_product_name_in_basket()
    actual_price = product_page.get_product_price_in_basket()

    assert actual_name == expected_name, f"Expected {expected_name}, got {actual_name}"
    assert (
        actual_price == expected_price
    ), f"Expected {expected_price}, got {actual_price}"
