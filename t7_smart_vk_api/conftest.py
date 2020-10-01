import pytest
from t7_smart_vk_api.browser.browser_factory import Browser
from t7_smart_vk_api.logger.logger import log
from t7_smart_vk_api import CONFIG_DATA


@pytest.fixture(params=[CONFIG_DATA["BROWSER"]], scope="session", autouse=True)
def browser(request):
    log.debug('Set-up')
    driver = Browser.get_browser_by_name(request.param)

    log.debug('Maximize browser window')
    driver.maximize_window()

    yield driver
    #
    # log.debug('Tear-down')
    # driver.quit()