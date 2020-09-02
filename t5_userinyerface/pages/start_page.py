from selenium.webdriver.common.by import By
from t5_userinyerface.default_page.default_page import BasePage
from t5_userinyerface.elements.base_element import Button


class StartPage(BasePage):

    CLICK_BUTTON = (By.XPATH, './/*[contains(@class, "start__link")]')
    #FIRST_CARD = (By.XPATH, './/*[text() = "1/4"]')


    def __init__(self, driver):
        super().__init__(driver)

    def click_on_link_to_next_page(self):
        Button(StartPage.CLICK_BUTTON, self.driver).click_on_button()

