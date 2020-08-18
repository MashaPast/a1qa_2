from selenium.webdriver.common.by import By
from t3_cookie.base_items.default_page import BasePage
from t3_cookie.base_items.element import BaseElement


class StartPage(BasePage):

    EXAMPLE_DOMAIN_HEADER = (By.TAG_NAME, 'h1')

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self):
        return BaseElement(StartPage.EXAMPLE_DOMAIN_HEADER, self.driver).get_text()

    def add_cookie(self, key_value):
        return self.driver.add_cookie(key_value)

    def get_cookie(self) -> list:
        return self.driver.get_cookies()

    def del_cookie(self, key):
        return self.driver.delete_cookie(key)

    def del_all_cookies(self):
        return self.driver.delete_all_cookies()

