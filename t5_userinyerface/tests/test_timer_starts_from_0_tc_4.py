from t5_userinyerface.pages.auth_page import AuthPage
from t5_userinyerface.pages.start_page import WelcomePage
from t5_userinyerface.helpers.loader import Loader
from t5_userinyerface.logger.logger import log
from t5_userinyerface import CONFIG_DATA

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_timer_tc_4(browser):
    log.info('Opening browser')
    welcome_page = WelcomePage(browser)
    log.info('Openning welcome page')
    welcome_page.open(CONFIG_DATA["URL"])

    log.info('Assert welcome page is opened')
    assert welcome_page.check_auth_page_is_open() is True

    log.info('Click to go the next page')
    welcome_page.click_on_link_to_next_page()

    log.info('Assert timer from null')
    auth_page = AuthPage(browser)
    assert auth_page.get_time_from_timer() == TEST_DATA["timer_value"]
