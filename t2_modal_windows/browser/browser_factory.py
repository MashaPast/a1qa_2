from t2_modal_windows.browser.singleton_get_browser import get_chrome, get_firefox
from t2_modal_windows.logger.logger import log


class Browser:
    @staticmethod
    def factory(browser_name: str):
        if browser_name == "Chrome":
            return Chrome().get_browser()
        if browser_name == "Firefox":
            return Firefox().get_browser()


class Chrome(Browser):
    def get_browser(self):
        log.debug('Get Chrome driver')
        driver = get_chrome()
        return driver


class Firefox(Browser):
    def get_browser(self):
        log.debug('Get Firefox driver')
        driver = get_firefox()
        return driver


