from pages.login_page import LoginPage


def test_guest_should_see_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_page()
