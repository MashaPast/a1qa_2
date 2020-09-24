from selenium.webdriver.common.by import By
from t7_smart_vk_api.base_items.default_page import BasePage
from t7_smart_vk_api.elements.button import Button
from t7_smart_vk_api.elements.field import Field


class WelcomePage(BasePage):
    EMAIL = Field((By.XPATH, '//input[contains(@id, "index_email")]'))
    PASS = Field((By.XPATH, '//input[contains(@id, "index_pass")]'))
    LOGIN = Button((By.XPATH, '//button[contains(@id, "index_login_button")]'))

    def __init__(self):
        super().__init__()

    def fill_email(self, email):
        self.EMAIL.send_text(email)

    def fill_password(self, password):
        self.PASS.send_text(password)

    def click_log_in(self):
        self.LOGIN.click()