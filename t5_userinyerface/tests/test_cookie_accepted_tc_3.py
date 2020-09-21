from t5_userinyerface.pages.auth_page import AuthPage
from t5_userinyerface.helpers.loader import Loader
from t5_userinyerface.logger.logger import log
from t5_userinyerface import CONFIG_DATA
from t5_userinyerface.pages.start_page import WelcomePage


TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_cookie_form():
    log.info('Opening browser')
    welcome_page = WelcomePage()
    log.info('Openning welcome page')
    welcome_page.open(CONFIG_DATA["URL"])

    log.info('Assert welcome page is opened')
    assert welcome_page.check_auth_page_is_open() is True

    log.info('Click to go the next page')
    welcome_page.click_on_link_to_next_page()

    log.info('Accept cookies')
    auth_page = AuthPage()
    auth_page.click_to_accept_cookie()

    log.info('Assert "Cookie" form is closed')
    assert auth_page.check_cookie_form_is_open() is False

    log.info('Assert "Cookie" accepted')
    assert auth_page.get_all_cookies() != []