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

    assert TEST_DATA["cookie1"]['name'] in start_page.get_cookie()[-1]['name']
    assert TEST_DATA["cookie2"]['name'] in start_page.get_cookie()[-2]['name']
    assert TEST_DATA["cookie3"]['name'] in start_page.get_cookie()[-3]['name']