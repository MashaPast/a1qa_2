from selenium.webdriver.remote.webelement import WebElement
from t4_iframe.pages.start_page import StartPage
from t4_iframe.helpers.loader import Loader
from t4_iframe.logger.logger import log
from t4_iframe import CONFIG_DATA
from t4_iframe.helpers.helpers import generate_random_text

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_iframe(browser):
    log.info('Opening browser')
    start_page = StartPage(browser)
    log.info('Openning page')
    start_page.go_to_site(CONFIG_DATA["URL"])

    log.info('Check http://the-internet.herokuapp.com/iframe is opened')
    assert start_page.get_header_text() == TEST_DATA["iFrame_header"]

    log.info('Switching to iFrame')
    start_page.switch_to_iframe()

    log.info('Clear iFrame field')
    start_page.clear_iframe_field()

    log.info('Send keys to iFrame field')
    random_str = generate_random_text()
    start_page.enter_text_in_iframe(TEST_DATA["text_to_enter"] + random_str)

    log.info('Check result with random string')
    assert start_page.get_text_from_iframe() == TEST_DATA["text_to_enter"] + random_str

    log.info('Highlight text')
    start_page.select_text_in_iframe()

    log.info('Click "B" button')
    start_page.switch_to_default_content()
    start_page.click_b_button()

    log.info('Check text is bold')
    assert start_page.check_strong_exists() == WebElement
