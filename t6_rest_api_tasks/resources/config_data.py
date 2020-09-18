from t6_rest_api_tasks.helpers.loader import Loader

CONFIG_DATA = Loader.get_config('./t6_rest_api_tasks/resources/configurations.json')

"""
setting environment variable for path to config before running tests
export CONFIG='./t6_rest_api_tasks/resources/configurations.json'

"""