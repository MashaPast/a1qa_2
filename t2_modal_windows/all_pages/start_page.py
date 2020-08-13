from selenium.webdriver.common.by import By
from t2_modal_windows.base_items.default_page import BasePage
from t2_modal_windows.base_items.element import Button, BaseElement
from selenium.webdriver.common.alert import Alert


class StartPageLocators:
    ALERT = (By.XPATH, '//*[@id="content"]//*[contains(text(), "Click for JS Alert")]')
    RESULT = (By.XPATH, '//*[@id="result"]')
    CONFIRM = (By.XPATH, '//*[@id="content"]//*[contains(text(), "Click for JS Confirm")]')
    PROMPT = (By.XPATH, '//*[@id="content"]//*[contains(text(), "Click for JS Prompt")]')


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_alert(self):
        button = Button(StartPageLocators.ALERT, self.driver)
        button.click()

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def accept_alert(self):
        Alert(self.driver).accept()

    def check_successfully_accept_alert(self):
        result = BaseElement(StartPageLocators.RESULT, self.driver)
        return result.get_text()

    def click_on_confirm(self):
        button = Button(StartPageLocators.CONFIRM, self.driver)
        button.click()

    def check_successfully_accept_confirm(self):
        result = BaseElement(StartPageLocators.RESULT, self.driver)
        return result.get_text()

    def click_on_js_prompt(self):
        button = Button(StartPageLocators.PROMPT, self.driver)
        button.click()

    def send_keys_in_modal_window(self, keys):
        Alert(self.driver).send_keys(keys)

    def check_successfully_send_keys(self):
        result = BaseElement(StartPageLocators.RESULT, self.driver)
        return result.get_text()
