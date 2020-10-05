from t7_smart_vk_api.pages.start_page import AuthPage
from t7_smart_vk_api.helpers.loader import Loader
from t7_smart_vk_api.logger.logger import log
from t7_smart_vk_api import CONFIG_DATA
from t7_smart_vk_api.helpers.utils import Utils
from t7_smart_vk_api.helpers.api_methods import APIClient, USER_ID
from t7_smart_vk_api.pages.user_page import UserPage

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])
post_text = Utils.generate_random_str()
edit_post_text = Utils.generate_random_str()
comment_to_post = Utils.generate_random_str()


def test_vk_wall():
    log.info('Opening browser')
    auth_page = AuthPage()
    log.info('Step 1. Openning vk.com welcome page')
    auth_page.open(CONFIG_DATA["URL"])

    log.info('Step 2. Authentication')
    auth_page.fill_email(TEST_DATA['email'])
    auth_page.fill_password(TEST_DATA['password'])
    auth_page.click_log_in()

    log.info('Step 3. Going to "My page"')
    user_page = UserPage()
    user_page.click_my_page()

    log.info('Step 4. Creating random post using API and get post id from response')
    post_message_response = APIClient.post_message(post_text)
    post_id = post_message_response['response']['post_id']

    log.info('Step 5. Checking that post is created with right text from right user')
    assert user_page.find_post(post_text)

    log.info('Step 6. Editing post using API - edit text and upload picture')
    picture = APIClient.upload_picture(TEST_DATA['PATH_TO_PIC'])["response"][0]["id"]
    APIClient.edit_post(post_id, edit_post_text, picture)

    log.info('Step 7. Checking that text is edited and picture is uploaded')

    log.info('Step 8. Add comment to post using API')
    APIClient.comment_post(post_id, comment_to_post)

    log.info('Step 9. Check comment is added from right user')
    user_post = '{}_{}'.format(USER_ID, post_id)
    user_page.show_comments_to_post(user_post)
    assert user_page.find_post(comment_to_post)
    assert user_page.get_comment_by_ids(user_post, USER_ID)

    log.info('Step 10. Using UI like the post')
    log.info('Post {}'.format(post_id))
    user_page.like_post(user_post)

    log.info('Step 11. Check like is added using API')
    assert APIClient.check_like(post_id)['response']['items'] == [USER_ID]

    log.info('Step 12. Delete post using API')
    APIClient.delete_post(post_id)

    log.info('Step 13. Check that post is deleted using UI')
    assert user_page.check_post_deleted(user_post) is True


