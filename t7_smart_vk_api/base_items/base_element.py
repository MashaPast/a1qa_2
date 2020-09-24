from abc import ABC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from t7_smart_vk_api import CONFIG_DATA
from t7_smart_vk_api.browser.browser_factory import Browser


class BaseElement(ABC):
    driver = Browser.get_browser_by_name(CONFIG_DATA["BROWSER"])

    def __init__(self, locator: tuple):
        """Initialize element with locator"""
        self.locator = locator

    def find_element(self, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(BaseElement.driver, time).until(EC.presence_of_element_located(self.locator),
                                                    message=f"Can't find element by locator {self.locator}")

    def find_elements(self, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(BaseElement.driver, time).until(EC.presence_of_element_located(self.locator),
                                                      message=f"Can't find element by locator {self.locator}")

    def get_text(self):
        return self.find_element().text

    def click(self):
        self.find_element().click()

    def send_text(self, text):
        return self.find_element().send_keys(text)