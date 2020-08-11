import requests
from requests.auth import HTTPBasicAuth
from t1_basic_authorization.config_loader import get_data

CONFIG_DATA = get_data("./t1_basic_authorization/config.json")
TEST_DATA = get_data("./t1_basic_authorization/t_data.json")


def make_auth_get_request():
    response = requests.get(CONFIG_DATA["URL"],
                            auth=HTTPBasicAuth(TEST_DATA['user'], TEST_DATA['pass']))
    return response


def get_response_body(response_for_body):
    body = response_for_body.json()
    return body
