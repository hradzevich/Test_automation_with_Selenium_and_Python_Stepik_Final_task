from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "id_login-username")
    PASSWORD_FIELD = (By.ID, "id_login-password")
    LOGIN_BTN = (By.XPATH, "//button[@name='login_submit']")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    PRODUCT_PRICE = (
        By.XPATH,
        "//div[contains(@class, 'product_main')]/p[@class='price_color']",
    )
    VIEW_BASKET_BTN = (
        By.XPATH,
        "//div[@class='alertinner']//a[text()='View basket']",
    )
    PRODUCT_NAME_IN_BASKET = (
        By.CSS_SELECTOR,
        "#messages > div:nth-child(1) > div > strong",
    )

    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alertinner p strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
