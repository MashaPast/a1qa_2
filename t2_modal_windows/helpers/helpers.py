import json
from os.path import abspath
import random
import string
from selenium.webdriver.common.by import By


class Loader:
    config = None
    asset = None

    @staticmethod
    def read_json_file(path) -> dict:
        with open(abspath(path)) as conf:
            data = json.load(conf)
            return data

    @staticmethod
    def get_config_data():
        if Loader.config is None:
            config = Loader.read_json_file('./t2_modal_windows/configs/config.json')
            return config
        else:
            return Loader.config

    @staticmethod
    def get_asset_data():
        if Loader.asset is None:
            asset = Loader.read_json_file('./t2_modal_windows/assets/asset.json')
            return asset
        else:
            return Loader.asset


def generate_random_text(n=20):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    return random_str


def build_locator(locator, param1: str):
    new_locator = (By.XPATH, locator.format(param1))
    return new_locator
