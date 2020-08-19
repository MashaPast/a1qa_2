from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from t3_cookie.helpers.helpers import Loader


CONFIG_DATA = Loader.get_config()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

