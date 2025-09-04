from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    EMAIL_FIELD = (By.ID, "id_login-username")
    PASSWORD_FIELD = (By.ID, "id_login-password")
    LOGIN_BTN = (By.XPATH, "//button[@name='login_submit']")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
