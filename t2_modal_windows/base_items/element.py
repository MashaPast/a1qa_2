from abc import ABC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from t2_modal_windows.helpers.helpers import Loader


CONFIG_DATA = Loader.get_config_data()


class BaseElement(ABC):
    def __init__(self, locator: tuple, driver):
        """Initialize element with locator"""
        self.locator = locator
        self.driver = driver

    def wait_text(self, text, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(self.locator, text),
                                                    message=f"Can't find element by locator {self.locator}")

    def get_text(self) -> str:
        return self.find_element().text

    def find_element(self, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.locator),
                                                    message=f"Can't find element by locator {self.locator}")


class Button(BaseElement):
    def __init__(self, locator, driver):
        super().__init__(locator, driver)

    def click(self):
        self.find_element().click()
