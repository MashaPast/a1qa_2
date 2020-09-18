import dataclasses
import json
from typing import Dict
import requests
from t6_rest_api_tasks import CONFIG_DATA
from t6_rest_api_tasks.logger.logger import log


class APIUtils:
    def __init__(self, url):
        self.url = url
        self.header = {'content-type': 'application/json'}

    def make_get_request(self, endpoint):
        log.info("Response to {}".format(endpoint))
        response = requests.get(self.url + endpoint)
        log.info("Response status is {}".format(response.status_code))
        return response

    def make_post_request(self, endpoint, body):
        log.info("Response to {}".format(endpoint))
        header = {"content-type": "application/json"}
        data = json.dumps(dataclasses.asdict(body))
        response = requests.post(self.url + endpoint, data=data, headers=header)
        log.info("Response status is {}".format(response.status_code))
        return response

    @staticmethod
    def get_response_body(response_for_body):
        body: list = response_for_body.json()
        log.info('Getting response body')
        return body

    @staticmethod
    def get_response_headers(response_for_headers):
        headers_data: Dict = dict(response_for_headers.headers)
        log.info('Getting response headers')
        return headers_data


api = APIUtils(CONFIG_DATA['URL'])