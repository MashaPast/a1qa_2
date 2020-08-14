from t2_modal_windows.all_pages.start_page import StartPage
from t2_modal_windows.helpers.helpers import Loader, generate_random_text
from t2_modal_windows.logger.logger import log


CONFIG_DATA = Loader.get_config_data()
ASSET = Loader.get_asset_data()


def test_modal_windows(browser):
    log.debug('Opening browser')
    start_page = StartPage(browser)
    log.debug('Open http://the-internet.herokuapp.com/javascript_alerts')
    start_page.go_to_site(CONFIG_DATA["URL"])

    log.debug('Click “Click for JS Alert” button')
    start_page.click_on_alert()

    log.debug('Switch to JS Alert')
    assert start_page.switch_to_alert()

    log.debug('Accept alert')
    start_page.accept_alert()

    log.debug('Check result')
    assert start_page.get_text_from_result_field() == ASSET["alert_success_result"]

    log.debug('Click “Click for JS Confirm” button')
    start_page.click_on_confirm()

    log.debug('Switch to JS Confirm')
    assert start_page.switch_to_alert()

    log.debug('Accept alert')
    start_page.accept_alert()

    log.debug('Check result')
    assert start_page.get_text_from_result_field() == ASSET["confirm_success_result"]

    log.debug('Click “Click for JS Prompt” button')
    start_page.click_on_js_prompt()

    log.debug('Switch to JS Prompt')
    assert start_page.switch_to_alert()

    log.debug('Send keys to JS Prompt')
    random_str = generate_random_text()
    start_page.send_keys_in_modal_window(random_str)

    log.debug('Accept alert')
    start_page.accept_alert()

    log.debug('Check result with random string')
    assert start_page.get_text_from_result_field() == ASSET["prompt_success_result"] + random_str

