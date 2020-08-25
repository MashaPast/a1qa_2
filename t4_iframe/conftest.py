import pytest
from t4_iframe.browser.browser_factory import Browser
from t4_iframe.logger.logger import log
from t4_iframe import CONFIG_DATA


@pytest.fixture(params=[CONFIG_DATA["BROWSER"]], scope="session")
def browser(request):
    log.debug('Set-up')
    driver = Browser.get_browser_by_name(request.param)

    log.debug('Maximize browser window')
    driver.maximize_window()

    yield driver

    log.debug('Tear-down')
    driver.quit()