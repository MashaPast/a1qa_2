from t6_rest_api_tasks.helpers.api_utils import api
from t6_rest_api_tasks import CONFIG_DATA
from http import HTTPStatus
from t6_rest_api_tasks.helpers.helpers import check_list_sorted_ascending, get_user_with_id_5
from t6_rest_api_tasks.helpers.loader import Loader
from t6_rest_api_tasks.resources.endpoints import all_posts, post_num_99, post_num_150, all_users, user_num_5
from t6_rest_api_tasks.resources.post_model import req_body
from t6_rest_api_tasks.logger.logger import log

TEST_DATA = Loader.read_json_file(CONFIG_DATA["ASSET_PATH"])


def test_get_all_posts():
    log.info('Step 1. Getting all posts')
    response = api.make_get_request(all_posts)
    body = api.get_response_body(response)
    headers = api.get_response_headers(response)

    log.info('Assert status_code from {} is 200'.format(all_posts))
    assert response.status_code == HTTPStatus.OK

    log.info('Assert response content-type is json')
    assert headers['Content-Type'] == TEST_DATA['content-type']

    log.info('Assert list of posts is sorted ascending')
    assert check_list_sorted_ascending(body) is True

    log.info('Step 2. Getting post num 99')
    response = api.make_get_request(post_num_99)
    body = api.get_response_body(response)

    log.info('Assert status_code from {} is 200'.format(post_num_99))
    assert response.status_code == HTTPStatus.OK

    log.info('Assert userId and id have correct values')
    assert body['userId'] == TEST_DATA['post_num_99']['userId']
    assert body['id'] == TEST_DATA['post_num_99']['id']

    log.info('Assert title and body are not empty strings')
    assert len(body['title']) != 0
    assert len(body['body']) != 0

    log.info('Step 3. Getting post num 150')
    response = api.make_get_request(post_num_150)
    body = api.get_response_body(response)

    log.info('Assert status_code from {} is 404'.format(post_num_150))
    assert response.status_code == HTTPStatus.NOT_FOUND

    log.info('Assert response body is empty')
    assert body == {}

    log.info('Step 4. Making post request')
    response = api.make_post_request(all_posts, req_body)
    res_body = api.get_response_body(response)

    log.info('Assert status_code from {} is 201'.format(all_posts))
    assert response.status_code == HTTPStatus.CREATED

    log.info('Assert title, body, userId are the same as in request')
    assert req_body.title == res_body['title']
    assert req_body.body == res_body['body']
    assert req_body.userId == res_body['userId']

    log.info('Assert id is in response body')
    assert res_body['id']

    log.info('Step 5. Getting all users')
    response = api.make_get_request(all_users)
    body = api.get_response_body(response)
    headers = api.get_response_headers(response)

    log.info('Assert status_code from {} is 200'.format(all_users))
    assert response.status_code == HTTPStatus.OK
    assert headers['Content-Type'] == TEST_DATA['content-type']

    log.info('Getting user_num_5 from response body'.format(all_users))
    user_5_from_resp = get_user_with_id_5(body)

    log.info('Assert user_num_5 from response body equals test data'.format(all_users))
    assert user_5_from_resp == TEST_DATA['user_num_5']

    log.info('Step 6. Getting user_num_5')
    response = api.make_get_request(user_num_5)
    body = api.get_response_body(response)
    headers = api.get_response_headers(response)

    log.info('Assert status_code from {} is 200'.format(user_num_5))
    assert response.status_code == HTTPStatus.OK
    log.info('Assert response content-type is json')
    assert headers['Content-Type'] == TEST_DATA['content-type']

    log.info('Assert response body from /users/5 equals response body from step 5')
    assert user_5_from_resp == body
