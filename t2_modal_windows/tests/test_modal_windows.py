from t2_modal_windows.all_pages.start_page import StartPage
from t2_modal_windows.helpers.helpers import Loader, generate_random_text
from t2_modal_windows.logger.logger import log


CONFIG_DATA = Loader.get_config_data()
TEST_DATA = Loader.get_asset_data()


def test_modal_windows(browser):
    log.info('Opening browser')
    start_page = StartPage(browser)
    log.info('Open http://the-internet.herokuapp.com/javascript_alerts')
    start_page.go_to_site(CONFIG_DATA["URL"])

    log.info('Click “Click for JS Alert” button')
    start_page.click_on_alert()

    log.info('Switch to JS Alert')
    assert start_page.switch_to_alert()

    log.info('Accept alert')
    start_page.accept_alert()

    log.info('Check result')
    assert start_page.get_text_from_result_field() == TEST_DATA["alert_success_result"]

    log.info('Click “Click for JS Confirm” button')
    start_page.click_on_confirm()

    log.info('Switch to JS Confirm')
    assert start_page.switch_to_alert()

    log.info('Accept alert')
    start_page.accept_alert()

    log.info('Check result')
    assert start_page.get_text_from_result_field() == TEST_DATA["confirm_success_result"]

    log.info('Click “Click for JS Prompt” button')
    start_page.click_on_js_prompt()

    log.info('Switch to JS Prompt')
    assert start_page.switch_to_alert()

    log.info('Send keys to JS Prompt')
    random_str = generate_random_text()
    start_page.send_keys_in_modal_window(random_str)

    log.info('Accept alert')
    start_page.accept_alert()

    log.info('Check result with random string')
    assert start_page.get_text_from_result_field() == TEST_DATA["prompt_success_result"] + random_str

