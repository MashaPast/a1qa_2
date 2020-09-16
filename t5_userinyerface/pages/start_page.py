from selenium.webdriver.common.by import By
from t5_userinyerface.base_items.default_page import BasePage
from t5_userinyerface.elements.button import Button


class WelcomePage(BasePage):
    CLICK_BUTTON = Button((By.XPATH, '//a[contains(@class, "start__link")]'))
    MAIN_LOGO = Button((By.XPATH, '//div[contains(@class, "logo__icon")]'))

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_link_to_next_page(self):
        self.CLICK_BUTTON.click()

    def check_auth_page_is_open(self):
        return self.MAIN_LOGO.check_form_exists()

