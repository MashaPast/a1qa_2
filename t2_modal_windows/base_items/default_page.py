from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from t2_modal_windows.helpers.helpers import Loader


CONFIG_DATA = Loader.get_config()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator, time=CONFIG_DATA["default_timeout"]):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

