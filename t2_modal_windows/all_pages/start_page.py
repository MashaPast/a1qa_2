from selenium.webdriver.common.by import By
from t2_modal_windows.base_items.default_page import BasePage
from t2_modal_windows.base_items.element import Button, BaseElement
from selenium.webdriver.common.alert import Alert
from t2_modal_windows.helpers.helpers import build_locator


class StartPage(BasePage):

    ALERT_BUTTON = '//*[@id="content"]//*[contains(text(), {})]'
    RESULT = (By.XPATH, '//*[@id="result"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_alert(self):
        alert = build_locator(By.XPATH, StartPage.ALERT_BUTTON, '"Click for JS Alert"')
        button = Button(alert, self.driver)
        button.click()

    def switch_to_alert(self):
        return self.driver.switch_to.alert

    def accept_alert(self):
        Alert(self.driver).accept()

    def get_text_from_result_field(self):
        result = BaseElement(StartPage.RESULT, self.driver)
        return result.get_text()

    def click_on_confirm(self):
        alert = build_locator(By.XPATH, StartPage.ALERT_BUTTON, '"Click for JS Confirm"')
        button = Button(alert, self.driver)
        button.click()

    def click_on_js_prompt(self):
        alert = build_locator(By.XPATH, StartPage.ALERT_BUTTON, '"Click for JS Prompt"')
        button = Button(alert, self.driver)
        button.click()

    def send_keys_in_modal_window(self, keys):
        Alert(self.driver).send_keys(keys)

