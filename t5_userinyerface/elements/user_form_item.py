from selenium.webdriver.support.select import Select

from t5_userinyerface.base_items.base_element import BaseElement


class UserFormItem(BaseElement):
    def __init__(self, locator: tuple, driver):
        super().__init__(locator, driver)

    def clear_field(self):
        return self.find_element().clear()

    def select_domain(self, domain):
        domain_form = self.find_element()
        select = Select(domain_form)
        select.select_by_visible_text(domain)