from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (
        By.XPATH,
        "//div[contains(@class, 'basket-mini')]//span[@class='btn-group']",
    )
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    EMAIL_LOGUN = (By.ID, "id_login-username")
    PASSWORD_LOGIN = (By.ID, "id_login-password")
    LOGIN_BTN = (By.XPATH, "//button[@name='login_submit']")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTER = (By.ID, "id_registration-email")
    PASSWORD_REGISTER_1 = (By.ID, "id_registration-password1")
    PASSWORD_REGISTER_2 = (By.ID, "id_registration-password2")
    REGISTER_BTN = (By.XPATH, "//button[@name='registration_submit']")


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


class BasketPageLocators:

    EMPTY_BASKET_TEXT = (By.XPATH, "//div[@id='content_inner']/p")

    ITEMS_IN_BASKET = (By.CLASS_NAME, "basket-items")
