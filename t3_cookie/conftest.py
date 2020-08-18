import pytest
from t3_cookie.browser.browser_factory import Browser
from t3_cookie.logger.logger import log
from t3_cookie.helpers.helpers import Loader

CONFIG_DATA = Loader.get_config()


@pytest.fixture(params=[CONFIG_DATA["BROWSER"]], scope="session")
def browser(request):
    log.debug('Set-up')
    driver = Browser.get_browser_by_name(request.param)

    log.debug('Maximize browser window')
    driver.maximize_window()

    yield driver

    log.debug('Tear-down')
    driver.quit()

