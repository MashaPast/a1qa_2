from selenium.webdriver.common.by import By
from t5_userinyerface.default_page.default_page import BasePage
from t5_userinyerface.elements.elements import Button


class StartPage(BasePage):

    CLICK_BUTTON = (By.XPATH, './/*[contains(@class, "start__link")]')
    MAIN_LOGO = (By.XPATH, './/*[contains(@class, "logo__icon")]')


    def __init__(self, driver):
        super().__init__(driver)

    def click_on_link_to_next_page(self):
        Button(StartPage.CLICK_BUTTON, self.driver).click_on_button()

    def check_auth_page_is_open(self):
        return Button(StartPage.MAIN_LOGO, self.driver).check_form_exists()

