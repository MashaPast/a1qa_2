import requests
from t7_smart_vk_api import CONFIG_DATA
from t7_smart_vk_api.helpers.loader import Loader
from t7_smart_vk_api.logger.logger import log

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])

API_VERS = TEST_DATA["API_VERS"]
URL = CONFIG_DATA['URL']
USER_ID = TEST_DATA['user_id']
API_URL = TEST_DATA["API_URL"]
TOKEN = TEST_DATA['token']


class APImethods:

    @staticmethod
    def post_message(message):
        log.info('{}wall.post?owner_id={}&message={}&access_token={}&v={}'.format(API_URL,
                                                                                  USER_ID, message, TOKEN, API_VERS))
        response = requests.post('{}wall.post?owner_id={}&message={}&access_token={}&v={}'.format(API_URL,
                                                                                                  USER_ID, message,
                                                                                                  TOKEN, API_VERS))
        body = response.json()
        log.info('Post message response body is {}'.format(body))
        return body

    @staticmethod
    def edit_post(post_id, message, picture):
        picture = 'photo{}_{}'.format(USER_ID, picture)
        response = requests.post('{}wall.edit?owner_id={}&message={}&attachment={}&post_id={}&access_token={}&v={}'.
                                 format(API_URL, USER_ID, message, picture, post_id, TOKEN, API_VERS))
        body = response.json()
        log.info('Edit post response body is {}'.format(body))
        return body

    @staticmethod
    def upload_picture(picture):
        upload_server_response = requests.get(
            '{}photos.getWallUploadServer?user_id={}&access_token={}&v={}'.format(API_URL, USER_ID, TOKEN, API_VERS)).\
            json()
        log.info('Get server to upload response body is {}'.format(upload_server_response))

        upload_picture_response = requests.post(
            upload_server_response['response']['upload_url'] + '&access_token={}&v={}'.format(TOKEN, API_VERS),
            files={'photo': open(picture, 'rb')}).json()
        log.info('Send file to upload_url response body is {}'.format(upload_picture_response))

        save_picture_response = requests.get(
            '{}photos.saveWallPhoto?user_id={}&photo={}&hash={}&server={}&access_token={}&v={}'
                .format(API_URL, USER_ID, upload_picture_response["photo"],
                        upload_picture_response["hash"], upload_picture_response["server"], TOKEN, API_VERS)).json()
        log.info('Save picture response body is {}'.format(save_picture_response))
        return save_picture_response["response"][0]["id"]

    @staticmethod
    def comment_post(post_id, comment):
        request = requests.get('{}wall.createComment?owner_id={}&post_id={}&message={}'
                               '&access_token={}&v={}'
                               .format(API_URL, USER_ID, post_id, comment, TOKEN, API_VERS)).json()
        return request

    @staticmethod
    def check_like(post_id):
        response = requests.get('{}likes.getList?type=post&user_id={}&item_id={}&access_token={}&v={}'
                                .format(API_URL, USER_ID, post_id, TOKEN, API_VERS)).json()
        log.info('Check like response body is {}'.format(response))
        return response['response']['items']

    @staticmethod
    def delete_post(post_id):
        response = requests.get('{}wall.delete?owner_id={}&post_id={}&access_token={}&v={}'.format(API_URL, USER_ID,
                                                                                                   post_id, TOKEN,
                                                                                                   API_VERS)).json()
        return response
