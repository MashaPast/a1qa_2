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
        if Loader.data is None:
            config = Loader.read_json_file(os.environ["CONFIG"])
            return config
        else:
            return Loader.data


