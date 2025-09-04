from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=20):
        self.browser = browser
        self.url = url
        self.wait = WebDriverWait(browser, timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def click_element(self, how, what):
        element = self.wait.until(EC.presence_of_element_located((how, what)))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def get_element_value(self, how, what):
        element = self.wait.until(EC.visibility_of_element_located((how, what)))
        return element.text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
