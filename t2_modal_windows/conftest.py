import pytest
from t2_modal_windows.browser.browser_factory import Browser
from t2_modal_windows.logger.logger import log
from t2_modal_windows.helpers.helpers import get_config_data

CONFIG_DATA = get_config_data()


@pytest.fixture(params=[CONFIG_DATA["BROWSER"]], scope="session")
def browser(request):
    log.debug('Set-up')
    driver = Browser.factory(request.param)

    log.debug('Maximize browser window')
    driver.maximize_window()

    yield driver

    log.debug('Tear-down')
    driver.quit()

