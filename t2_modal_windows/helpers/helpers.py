import json
from os.path import abspath
import random
import string

cache = {}
cache2 = {}


def get_config_data():
    if cache.get('config_data'):
        return cache.get('config_data')

    with open(abspath('./t2_modal_windows/configs/config.json')) as conf:
        data = json.load(conf)
        cache['config_data'] = data
        return data


CONFIG_DATA = get_config_data()


def get_asset_data():
    if cache2.get('test_data'):
        return cache2.get('test_data')

    with open(abspath('./t2_modal_windows/assets/asset.json')) as conf:
        data = json.load(conf)
        cache2['test_data'] = data
        return data


def generate_random_text():
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
    return random_str

