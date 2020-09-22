import dataclasses
import json
import requests
from t6_rest_api_tasks import CONFIG_DATA
from t6_rest_api_tasks.logger.logger import log


class APImethods:
    def __init__(self, url):
        self.url = url
        self.header = {'content-type': 'application/json'}

    def make_get_request(self, endpoint):
        log.info("GET request to {}".format(endpoint))
        response = requests.get(self.url + endpoint)
        log.info("Response status is {}".format(response.status_code))
        return response

    def make_post_request(self, endpoint, body):
        log.info("POST request to {}".format(endpoint))
        data = json.dumps(dataclasses.asdict(body))
        response = requests.post(self.url + endpoint, data=data, headers=self.header)
        log.info("Response status is {}".format(response.status_code))
        return response



api = APImethods(CONFIG_DATA['URL'])