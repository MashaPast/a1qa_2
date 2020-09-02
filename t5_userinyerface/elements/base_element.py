from abc import ABC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from t5_userinyerface import CONFIG_DATA


class BaseElement(ABC):
    def __init__(self, locator: tuple, driver):
        """Initialize element with locator"""
        self.locator = locator
        self.driver = driver

    def find_element(self, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.locator),
                                                    message=f"Can't find element by locator {self.locator}")


class Button(BaseElement):
    def click_on_button(self):
        self.find_element().click()

    def check_form_exists(self):
        try:
            self.find_element()
            return True
        except TimeoutException:
            return False

    def get_text(self):
        return self.find_element().text
