from t5_userinyerface.pages.auth_page import AuthPage
from t5_userinyerface.pages.start_page import StartPage
from t5_userinyerface.helpers.loader import Loader
from t5_userinyerface.logger.logger import log
from t5_userinyerface import CONFIG_DATA

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_userinyrface(browser):
    log.info('Opening browser')
    start_page = StartPage(browser)
    log.info('Openning page')
    start_page.go_to_site(CONFIG_DATA["URL"])

    log.info('Assert welcome page is opened')
    assert start_page.check_auth_page_is_open() == True

    log.info('Click to go the next page')
    start_page.click_on_link_to_next_page()

    log.info('Assert timer from null')
    auth_page = AuthPage(browser)
    assert auth_page.get_time_from_timer() == TEST_DATA["timer_value"]
