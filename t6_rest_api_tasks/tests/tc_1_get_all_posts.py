import pytest
from t6_rest_api_tasks.helpers.api_utils import APIUtils
from t6_rest_api_tasks import CONFIG_DATA
from http import HTTPStatus

from t6_rest_api_tasks.helpers.helpers import check_list_sorted_ascending

ob = APIUtils(CONFIG_DATA['URL'])


def test_get_all_posts():
    response = ob.make_get_request('/posts')
    body = ob.get_response_body(response)
    headers = ob.get_response_headers(response)

    assert response.status_code == HTTPStatus.OK
    assert headers['Content-Type'] == 'application/json; charset=utf-8'
    assert check_list_sorted_ascending(body) is True


def test_get_post_num99():
    response = ob.make_get_request('/posts/99')
    body = ob.get_response_body(response)

    assert response.status_code == HTTPStatus.OK
    assert body['userId'] == 10
    assert body['id'] == 99
    assert body['title']
    assert body['body']


def test_get_post_num150():
    response = ob.make_get_request('/posts/150')
    body = ob.get_response_body(response)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert body == {}