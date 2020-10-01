from selenium.webdriver.support.wait import WebDriverWait
from t7_smart_vk_api.browser.browser_factory import Browser
from t7_smart_vk_api.resources.config_data import CONFIG_DATA
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    driver = Browser.get_browser_by_name(CONFIG_DATA["BROWSER"])

    def __init__(self):
        pass

    def open(self, url):
        return self.driver.get(url)

    def find_element(self, locator, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
