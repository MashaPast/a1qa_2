from abc import ABC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from t4_iframe import CONFIG_DATA


class BaseElement(ABC):
    def __init__(self, locator: tuple, driver):
        """Initialize element with locator"""
        self.locator = locator
        self.driver = driver

    def find_element(self, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(self.locator),
                                                    message=f"Can't find element by locator {self.locator}")


class Header(BaseElement):
    def get_header_text(self) -> str:
        return self.find_element().text


class Iframe(BaseElement):
    def find_and_switch_to_iframe(self):
        iframe = self.find_element()
        return self.driver.switch_to.frame(iframe)

    def clear_text(self) -> str:
        return self.find_element().clear()

    def send_keys_to_iframe(self, keys):
        return self.find_element().send_keys(keys)

    def get_text_from_iframe(self):
        return self.find_element().text

    def highlight_text_in_iframe(self):
        return self.find_element().send_keys(Keys.CONTROL, "a")


class Button(BaseElement):
    def click_on_button(self):
        self.find_element().click()

    def check_strong_element_exists(self):
        self.find_element()