from t5_userinyerface.pages.auth_page import UserFormAuthPage
from t5_userinyerface.pages.interests_page import InterestsPage
from t5_userinyerface.pages.start_page import WelcomePage
from t5_userinyerface.helpers.loader import Loader
from t5_userinyerface.logger.logger import log
from t5_userinyerface import CONFIG_DATA

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_user_form(browser):
    log.info('Opening browser')
    welcome_page = WelcomePage(browser)
    log.info('Openning welcome page')
    welcome_page.open(CONFIG_DATA["URL"])

    log.info('Assert welcome page is opened')
    assert welcome_page.check_auth_page_is_open() == True

    log.info('Click to go the next page')
    welcome_page.click_on_link_to_next_page()

    log.info('Assert first card to enter information is opened')
    user_form_auth_page = UserFormAuthPage(browser)
    assert user_form_auth_page.check_card_is_opened() == TEST_DATA["first_card_number"]

    log.info('Enter correct password, email and accept terms. Click "next"')
    user_form_auth_page.clear_pass()
    user_form_auth_page.clear_email()
    user_form_auth_page.clear_domain()

    user_form_auth_page.fill_pass()
    user_form_auth_page.fill_email()
    user_form_auth_page.fill_domain(TEST_DATA["domain"])

    user_form_auth_page.click_to_accept_terms()
    user_form_auth_page.click_next()

    user_form_auth_page.select_domain_in_drop_down(TEST_DATA["domain_to_select"])

    log.info('Assert second card to enter information is opened')
    assert user_form_auth_page.check_card_is_opened() == TEST_DATA["second_card_number"]

    log.info('Select 3 random interests, upload image. Click "next"')
    interests_page = InterestsPage(browser)
    interests_page.unselect_in_checkbox()
    interests_page.select_in_checkbox()

    interests_page.upload_image(TEST_DATA['path'])


    # log.info('Assert third card to enter information is opened')
    # assert user_form_auth_page.check_card_is_opened() == TEST_DATA["third_card_number"]
