from t5_userinyerface.browser.browser_factory import Browser
from t5_userinyerface.resources.config_data import CONFIG_DATA


class BasePage:
    driver = Browser.get_browser_by_name(CONFIG_DATA["BROWSER"])

    def __init__(self, driver):
        pass


    def open(self, url):
        return self.driver.get(url)