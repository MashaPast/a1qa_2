import json
from os.path import abspath
import random
import string
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


def generate_random_text(n=20):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    return random_str


def build_locator(locator_type, locator, button_text: str):
    new_locator = (locator_type, locator.format(button_text))
    return new_locator
