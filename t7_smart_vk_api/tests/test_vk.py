from t7_smart_vk_api.pages.start_page import WelcomePage
from t7_smart_vk_api.helpers.loader import Loader
from t7_smart_vk_api.logger.logger import log
from t7_smart_vk_api import CONFIG_DATA

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_vk():
    log.info('Opening browser')
    welcome_page = WelcomePage()
    log.info('Step 1. Openning vk.com welcome page')
    welcome_page.open(CONFIG_DATA["URL"])

    log.info('Step 2. Authentication')
    welcome_page.fill_email(TEST_DATA['email'])
    welcome_page.fill_password(TEST_DATA['password'])
    welcome_page.click_log_in()

    log.info('Step 3. Going to "My page"')
    log.info('Step 4. Creating random post using API and get post id from response')
    log.info('Step 5. Checking that post is created with right text from right user')
    log.info('Step 6. Editing post using API - edit text and upload picture')
    log.info('Step 7. Checking that text is edited  and picture is uploaded')
    log.info('Step 8. Add comment to post using API')
    log.info('Step 9. Check comment is added')
    log.info('Step 10. Using UI like the post')
    log.info('Step 11. Check like is added using API')
    log.info('Step 12. Delete post using API')
    log.info('Step 13. Check that post is deleted using UI')



    # log.info('Assert welcome page is opened')
    # assert welcome_page.check_auth_page_is_open() == True
    #
    # log.info('Click to go the next page')
    # welcome_page.click_on_link_to_next_page()
    #
    # log.info('Assert first card to enter information is opened')
    # user_form_auth_page = UserFormAuthPage()
    # assert user_form_auth_page.check_card_is_opened() == TEST_DATA["first_card_number"]
    #
    # log.info('Clear password, email and accept terms')
    # user_form_auth_page.clear_pass()
    # user_form_auth_page.clear_email()
    # user_form_auth_page.clear_domain()
    #
    # log.info('Enter correct password, email and accept terms')
    # user_form_auth_page.fill_pass()
    # user_form_auth_page.fill_email()
    # user_form_auth_page.fill_domain(TEST_DATA["domain"])
    #
    # log.info('Click to accept terms')
    # user_form_auth_page.click_to_accept_terms()
    #
    #
    #
    # log.info('Select domain')
    # user_form_auth_page.click_drop_down_menu()
    # user_form_auth_page.select_org_domain()
    #
    # log.info('Click "next"')
    # user_form_auth_page.click_next()
    #
    # log.info('Assert second card to enter information is opened')
    # assert user_form_auth_page.check_card_is_opened() == TEST_DATA["second_card_number"]
    #
    # log.info('Select 3 random interests')
    # interests_page = InterestsPage()
    # interests_page.unselect_in_checkbox()
    # interests_page.select_in_checkbox()
    #
    # log.info('Upload image')
    # interests_page.upload_image()