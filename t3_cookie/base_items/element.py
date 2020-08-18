from abc import ABC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from t3_cookie.helpers.helpers import Loader


CONFIG_DATA = Loader.get_config()


class BaseElement(ABC):
    def __init__(self, locator: tuple, driver):
        """Initialize element with locator"""
        self.locator = locator
        self.driver = driver

    def get_text(self) -> str:
        return self.find_element().text

    def find_element(self, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.locator),
                                                    message=f"Can't find element by locator {self.locator}")

