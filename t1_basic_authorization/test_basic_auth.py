from t1_basic_authorization.config_loader import get_data
from t1_basic_authorization.helpers import make_auth_get_request, get_response_body
from http import HTTPStatus

ASSET = get_data("./t1_basic_authorization/asset.json")


def test_basic_auth():
    response = make_auth_get_request()
    assert response.status_code == HTTPStatus.OK
    body = get_response_body(response)
    assert body == ASSET