from t5_userinyerface.helpers.loader import Loader

CONFIG_DATA = Loader.get_config('./t5_userinyerface/resources/configurations.json')

"""
setting environment variable for path to config before running tests:
export CONFIG = './t5_userinyerface/resources/configurations.json'
"""