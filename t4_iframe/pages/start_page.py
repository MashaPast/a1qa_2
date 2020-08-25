from selenium.webdriver.common.by import By
from t4_iframe.default_page.default_page import BasePage
from t4_iframe.elements.base_element import Header, Iframe, Button


class StartPage(BasePage):

    IFRAME_HEADER = (By.TAG_NAME, 'h3')
    FIELD = (By.XPATH, '//*[@id="tinymce"]/p')
    IFRAME = (By.ID, 'mce_0_ifr')
    B_BUTTON = (By.XPATH, '//div[@aria-label="Bold"]')
    P_STRONG = (By.XPATH, '//div[@aria-level="1"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_header_text(self):
        return Header(StartPage.IFRAME_HEADER, self.driver).get_header_text()

    def clear_iframe_field(self):
        return Iframe(StartPage.FIELD, self.driver).clear_text()

    def switch_to_iframe(self):
        return Iframe(StartPage.IFRAME, self.driver).find_and_switch_to_iframe()

    def enter_text_in_iframe(self, keys):
        Iframe(StartPage.FIELD, self.driver).send_keys_to_iframe(keys)

    def get_text_from_iframe(self):
        return Iframe(StartPage.FIELD, self.driver).get_text_from_iframe()

    def select_text_in_iframe(self):
        return Iframe(StartPage.FIELD, self.driver).highlight_text_in_iframe()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def click_b_button(self):
        Button(StartPage.B_BUTTON, self.driver).click_on_button()

    def check_strong_exists(self):
        return type(Button(StartPage.P_STRONG, self.driver).find_element())
