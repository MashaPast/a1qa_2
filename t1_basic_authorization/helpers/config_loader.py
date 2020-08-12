import json
from os.path import abspath


def get_data(path):
    with open(abspath(path)) as conf:
        data = json.load(conf)
        return data