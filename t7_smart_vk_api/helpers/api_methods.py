import requests
from t7_smart_vk_api import CONFIG_DATA
from t7_smart_vk_api.helpers.loader import Loader
from t7_smart_vk_api.logger.logger import log

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


class APIClient:
    API_VERSION = TEST_DATA["API_VERS"]
    URL = CONFIG_DATA['URL']
    USER_ID = TEST_DATA['user_id']
    API_URL = TEST_DATA["API_URL"]
    TOKEN = TEST_DATA['token']

    @staticmethod
    def post_message(message):
        response = requests.post(f'{APIClient.API_URL}wall.post?owner_id={APIClient.USER_ID}&message={message}'
                                 f'&access_token={APIClient.TOKEN}&v={APIClient.API_VERSION}').json()
        log.info('Post message response body is {}'.format(response))
        return response

    @staticmethod
    def edit_post(post_id, message, picture):
        picture = f'photo{APIClient.USER_ID}_{picture}'
        response = requests.post(f'{APIClient.API_URL}wall.edit?owner_id={APIClient.USER_ID}'
                                 f'&message={message}&attachment={picture}'
                                 f'&post_id={post_id}&access_token={APIClient.TOKEN}&v={APIClient.API_VERSION}').json()
        log.info('Edit post response body is {}'.format(response))
        return response

    @staticmethod
    def upload_picture(picture):
        upload_server_response = requests.get(
            f'{APIClient.API_URL}photos.getWallUploadServer?user_id={APIClient.USER_ID}'
            f'&access_token={APIClient.TOKEN}&v={APIClient.API_VERSION}').json()
        log.info('Get server to upload response body is {}'.format(upload_server_response))

        upload_picture_response = requests.post(
            upload_server_response['response']['upload_url'] + f'&access_token={APIClient.TOKEN}'
                                                               f'&v={APIClient.API_VERSION}',
            files={'photo': open(picture, 'rb')}).json()
        log.info('Send file to upload_url response body is {}'.format(upload_picture_response))

        save_picture_response = requests.get(
            f'{APIClient.API_URL}photos.saveWallPhoto?user_id={APIClient.USER_ID}'
            f'&photo={upload_picture_response["photo"]}&hash={upload_picture_response["hash"]}'
            f'&server={upload_picture_response["server"]}&access_token={APIClient.TOKEN}'
            f'&v={APIClient.API_VERSION}').json()
        log.info('Save picture response body is {}'.format(save_picture_response))
        return save_picture_response

    @staticmethod
    def comment_post(post_id, comment):
        response = requests.get(f'{APIClient.API_URL}wall.createComment?owner_id={APIClient.USER_ID}&post_id={post_id}'
                                f'&message={comment}&access_token={APIClient.TOKEN}&v={APIClient.API_VERSION}').json()
        return response

    @staticmethod
    def check_like(post_id):
        response = requests.get(f'{APIClient.API_URL}likes.getList?type=post&user_id={APIClient.USER_ID}'
                                f'&item_id={post_id}&access_token={APIClient.TOKEN}&v={APIClient.API_VERSION}').json()
        log.info('Check like response body is {}'.format(response))
        return response

    @staticmethod
    def delete_post(post_id):
        response = requests.get(f'{APIClient.API_URL}wall.delete?owner_id={APIClient.USER_ID}&post_id={post_id}'
                                f'&access_token={APIClient.TOKEN}&v={APIClient.API_VERSION}').json()
        return response
