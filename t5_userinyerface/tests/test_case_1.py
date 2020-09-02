from t5_userinyerface.pages.start_page import StartPage
from t5_userinyerface.helpers.loader import Loader
from t5_userinyerface.logger.logger import log
from t5_userinyerface import CONFIG_DATA
from t5_userinyerface.helpers.helpers import generate_random_text

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_userinyrface(browser):
    log.info('Opening browser')
    start_page = StartPage(browser)
    log.info('Openning page')
    start_page.go_to_site(CONFIG_DATA["URL"])

    log.info('Check https://userinyerface.com/game.html%20target= is opened')
    # assert start_page.get_header_text() == TEST_DATA["iFrame_header"]

    log.info('Click to go the next page')
    start_page.click_on_link_to_next_page()

    log.info('Assert first card to enter information is opened')

    log.info('Enter correct password, email and accept terms. Click "next"')

    log.info('Assert second card to enter information is opened')

    log.info('Select 3 random interests, upload image. Click "next')

    log.info('Assert third card to enter information is opened')
