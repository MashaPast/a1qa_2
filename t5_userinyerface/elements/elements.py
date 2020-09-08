import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

from t5_userinyerface.elements.base_element import BaseElement


class UserForm:
    def __init__(self, locator_res: tuple, driver):
        self.auth = Item(locator_res, driver)


class Item(BaseElement):
    def __init__(self, locator: tuple, driver):
        super().__init__(locator, driver)

    def click(self):
        self.find_element().click()

    def get_num_of_card(self):
        return self.find_element().text

    def clear_field(self):
        return self.find_element().clear()

    def send_text(self, text):
        return self.find_element().send_keys(text)

    def select_domain(self, domain):
        domain_form = self.find_element()
        select = Select(domain_form)
        select.select_by_visible_text(domain)




class Button(BaseElement):
    def click_on_button(self):
        self.find_element().click()

    def upload_image(self, path):
        self.find_element().send_keys(path)

    def check_form_exists(self):
        try:
            self.find_element()
            return True
        except TimeoutException:
            return False


    def get_text(self):
        return self.find_element().text


class CheckBox(BaseElement):
    def select_in_checkbox(self):
        self.find_element().click()