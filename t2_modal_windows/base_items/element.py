from abc import ABC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(ABC):
    def __init__(self, locator: tuple, driver):
        """Initialize element with locator"""
        self.locator = locator
        self.driver = driver

    def wait_text(self, text):
        return WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.locator, text),
                                                    message=f"Can't find element by locator {self.locator}")

    def get_text(self) -> str:
        return self.find_element().text

    def find_element(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.locator),
                                                    message=f"Can't find element by locator {self.locator}")


class Button(BaseElement):
    def __init__(self, locator, driver):
        super().__init__(locator, driver)

    def click(self):
        self.find_element().click()
