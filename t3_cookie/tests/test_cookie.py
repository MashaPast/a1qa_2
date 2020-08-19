from t3_cookie.all_pages.start_page import StartPage
from t3_cookie.helpers.helpers import Loader
from t3_cookie.logger.logger import log


CONFIG_DATA = Loader.get_config()
TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_cookie(browser):
    log.info('Opening browser')
    start_page = StartPage(browser)
    log.info('Open http://example.com/')
    start_page.go_to_site(CONFIG_DATA["URL"])

    log.info('Check http://example.com/ is opened')
    assert start_page.get_header_text() == 'Example Domain'

    log.info('Add cookie')
    start_page.add_cookie(TEST_DATA["cookie1"])
    start_page.add_cookie(TEST_DATA["cookie2"])
    start_page.add_cookie(TEST_DATA["cookie3"])

    log.info('Check cookie added')
    assert start_page.get_cookie_by_name(TEST_DATA["cookie1"]['name']) is not None
    assert start_page.get_cookie_by_name(TEST_DATA["cookie2"]['name']) is not None
    assert start_page.get_cookie_by_name(TEST_DATA["cookie3"]['name']) is not None

    log.info('Delete cookie with example_key_1')
    start_page.del_cookie_by_name(TEST_DATA["cookie1"]['name'])

    log.info('Check cookie deleted')
    assert start_page.get_cookie_by_name(TEST_DATA["cookie1"]['name']) is None

    log.info('Add example_value_300 for cookie with example_key_3')
    start_page.add_cookie(TEST_DATA["updated_value_cookie"])

    log.info('Check cookie value is updated')
    assert start_page.get_cookie_value(TEST_DATA["updated_value_cookie"]['name']) == TEST_DATA["updated_value_cookie"]['value']

    log.info('Delete all cookie')
    start_page.del_all_cookies()

    log.info('Check cookie deleted')
    assert start_page.get_all_cookies() == []