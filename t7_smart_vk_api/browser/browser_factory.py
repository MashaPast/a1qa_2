from enum import Enum
from t7_smart_vk_api.logger.logger import log
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class SupportedBrowsers(Enum):
    Chrome = 'Chrome'
    Firefox = 'Firefox'


class Browser:
    @staticmethod
    def get_browser_by_name(browser_name: str):
        if browser_name == SupportedBrowsers.Chrome.value:
            return Chrome.get_driver()
        if browser_name == SupportedBrowsers.Firefox.value:
            return Firefox.get_driver()


class Chrome(Browser):
    instance = None

    @staticmethod
    def get_driver():
        log.debug('Get Chrome driver')
        if Chrome.instance is None:
            Chrome.instance = webdriver.Chrome(ChromeDriverManager().install(), service_log_path='/dev/null')
            return Chrome.instance
        else:
            return Chrome.instance


class Firefox(Browser):
    instance = None

    @staticmethod
    def get_driver():
        log.debug('Get Firefox driver')
        if Firefox.instance is None:
            Firefox.instance = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            return Firefox.instance
        else:
            return Firefox.instance