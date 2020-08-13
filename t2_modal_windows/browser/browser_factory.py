from t2_modal_windows.browser.singleton_get_browser import get_chrome, get_firefox
from t2_modal_windows.logger.logger import appLogger


class Browser:
    def factory(browser_name: str):
        if browser_name == "Chrome":
            return Chrome().browser()
        if browser_name == "Firefox":
            return Firefox().browser()

    factory = staticmethod(factory)


class Chrome(Browser):
    def browser(self):
        appLogger.debug('Get Chrome driver')
        driver = get_chrome()
        return driver


class Firefox(Browser):
    def browser(self):
        appLogger.debug('Get Firefox driver')
        driver = get_firefox()
        return driver


