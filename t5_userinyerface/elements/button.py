from selenium.common.exceptions import TimeoutException

from t5_userinyerface.base_items.base_element import BaseElement


class Button(BaseElement):
    def __init__(self, locator: tuple):
        super().__init__(locator)

    def upload_image(self, path):
        self.find_element().send_keys(path)

    def check_form_exists(self):
        try:
            self.find_element()
            return True
        except TimeoutException:
            return False