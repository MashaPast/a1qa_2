import json
from os.path import abspath
import os


class Loader:
    data = None

    @staticmethod
    def read_json_file(path) -> dict:
        with open(abspath(path)) as conf:
            data = json.load(conf)
            return data

    @staticmethod
    def get_config():
        """
        setting environment variable for path to config before running tests
        export CONFIG='./t6_rest_api_tasks/resources/configurations.json'

        """
        if Loader.data is None:
            path = os.environ["CONFIG"]
            if path is None:
                path = './t6_rest_api_tasks/resources/configurations.json'
            config = Loader.read_json_file(path)
            return config
        else:
            return Loader.data