from selenium.webdriver.common.by import By
from t5_userinyerface.default_page.default_page import BasePage
from t5_userinyerface.elements.base_element import Button


class AuthPage(BasePage):

    COOKIE_FORM = (By.XPATH, '//*[@id="app"]/div/div[1]')#'.//*[contains(@class, "cookies")]')
    ACCEPT_COOKIE = (By.XPATH, './/*[text() = "Not really, no"]')
    SEND_TO_BUTTON = (By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[2]/button')
    HELP_FORM_IS_HIDDEN = (By.XPATH, './/*[contains(@class, "help-form is-hidden")]')
    TIMER = (By.XPATH, './/*[contains(@class, "timer timer--white timer--center")]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_send_to_button(self):
        return Button(AuthPage.SEND_TO_BUTTON, self.driver).click_on_button()

    def check_help_window_is_closed(self):
        return Button(AuthPage.HELP_FORM_IS_HIDDEN, self.driver).check_form_exists()

    def get_time_from_timer(self):
        return Button(AuthPage.TIMER, self.driver).get_text()