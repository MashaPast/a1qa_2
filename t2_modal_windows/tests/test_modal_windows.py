from t2_modal_windows.all_pages.start_page import StartPage
from t2_modal_windows.helpers.helpers import get_config_data, get_asset_data, generate_random_text
from t2_modal_windows.logger.logger import appLogger


CONFIG_DATA = get_config_data()
ASSET = get_asset_data()


def test_modal_windows(browser):
    appLogger.debug('Opening browser')
    start_page = StartPage(browser)
    appLogger.debug('Open http://the-internet.herokuapp.com/javascript_alerts')
    start_page.go_to_site(CONFIG_DATA["URL"])

    appLogger.debug('Click “Click for JS Alert” button')
    start_page.click_on_alert()

    appLogger.debug('Switch to JS Alert')
    assert start_page.switch_to_alert()

    appLogger.debug('Accept alert')
    start_page.accept_alert()

    appLogger.debug('Check result')
    assert start_page.check_successfully_accept_alert() == ASSET["alert_success_result"]

    appLogger.debug('Click “Click for JS Confirm” button')
    start_page.click_on_confirm()

    appLogger.debug('Switch to JS Confirm')
    assert start_page.switch_to_alert()

    appLogger.debug('Accept alert')
    start_page.accept_alert()

    appLogger.debug('Check result')
    assert start_page.check_successfully_accept_confirm() == ASSET["confirm_success_result"]

    appLogger.debug('Click “Click for JS Prompt” button')
    start_page.click_on_js_prompt()

    appLogger.debug('Switch to JS Prompt')
    assert start_page.switch_to_alert()

    appLogger.debug('Send keys to JS Prompt')
    random_str = generate_random_text()
    start_page.send_keys_in_modal_window(random_str)

    appLogger.debug('Accept alert')
    start_page.accept_alert()

    appLogger.debug('Check result with random string')
    assert start_page.check_successfully_send_keys() == ASSET["prompt_success_result"] + random_str

