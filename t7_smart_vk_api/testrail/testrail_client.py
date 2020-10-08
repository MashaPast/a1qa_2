from t7_smart_vk_api.testrail.testrail import *
from t7_smart_vk_api.testrail.config_parser import config

tr_config = config["API"]

client = APIClient(tr_config['url'])
client.user = tr_config['user']
client.password = tr_config['password']

screenshot = tr_config['screenshot']
tr_run_id = tr_config['tr_run_id']