from t7_smart_vk_api.helpers.loader import Loader

CONFIG_DATA = Loader.get_config('./t7_smart_vk_api/resources/configurations.json')

"""
setting environment variable for path to config before running tests:
export CONFIG = './t7_smart_vk_api/resources/configurations.json'
"""