from t7_smart_vk_api.browser.browser_factory import Browser
from t7_smart_vk_api.resources.config_data import CONFIG_DATA


class BasePage:
    driver = Browser.get_browser_by_name(CONFIG_DATA["BROWSER"])

    def __init__(self):
        pass

    def open(self, url):
        return self.driver.get(url)