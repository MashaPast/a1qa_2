from selenium.webdriver.common.by import By
from t3_cookie.base_items.default_page import BasePage
from t3_cookie.base_items.element import BaseElement
from t3_cookie.helpers.helpers import Loader

CONFIG_DATA = Loader.get_config()
TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


class StartPage(BasePage):

    EXAMPLE_DOMAIN_HEADER = (By.TAG_NAME, 'h1')

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self):
        return BaseElement(StartPage.EXAMPLE_DOMAIN_HEADER, self.driver).get_text()

    def add_cookie(self, key_value):
        return self.driver.add_cookie(key_value)

    def get_all_cookies(self) -> list:
        return self.driver.get_cookies()

    def get_cookie_by_name(self, cookie_name) -> dict:
        return self.driver.get_cookie(cookie_name)

    def del_cookie_by_name(self, cookie_name):
        return self.driver.delete_cookie(cookie_name)

    def get_cookie_value(self, cookie_name) -> str:
        return self.driver.get_cookie(cookie_name)['value']

    def del_all_cookies(self):
        return self.driver.delete_all_cookies()

