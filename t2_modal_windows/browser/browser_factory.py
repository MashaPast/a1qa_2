from t2_modal_windows.logger.logger import log
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class Browser:
    @staticmethod
    def get_browser_by_name(browser_name: str):
        if browser_name == "Chrome":
            return Chrome().get_browser()
        if browser_name == "Firefox":
            return Firefox().get_browser()


class Chrome(Browser):
    instance = None

    @staticmethod
    def get_browser():
        """
        :return: <class 'selenium.webdriver.chrome.webdriver.WebDriver'>
        """
        log.debug('Get Chrome driver')
        if Chrome.instance is None:
            Chrome.instance = webdriver.Chrome(ChromeDriverManager().install(), service_log_path='/dev/null')
            return Chrome.instance
        else:
            return Chrome.instance


class Firefox(Browser):
    instance = None

    @staticmethod
    def get_browser():
        """
        :return: <class 'selenium.webdriver.chrome.webdriver.WebDriver'>
        """
        log.debug('Get Firefox driver')
        if Firefox.instance is None:
            Firefox.instance = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            return Firefox.instance
        else:
            return Firefox.instance

