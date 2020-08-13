import pytest
from t2_modal_windows.browser.browser_factory import Browser
from t2_modal_windows.logger import appLogger
from t2_modal_windows.helpers.helpers import get_config_data

CONFIG_DATA = get_config_data()


@pytest.fixture(params=[CONFIG_DATA["BROWSER"]], scope="session")
def browser(request):
    appLogger.debug('Set-up')
    driver = Browser.factory(request.param)

    appLogger.debug('Maximize browser window')
    driver.maximize_window()

    yield driver

    appLogger.debug('Tear-down')
    driver.quit()

