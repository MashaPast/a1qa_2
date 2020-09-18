import logging
import os
from t6_rest_api_tasks import CONFIG_DATA
import time

timestamp = int(time.time())
logs_dir = CONFIG_DATA["LOG_DIR"]

if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)

logging.basicConfig(filename=CONFIG_DATA["LOG_DIR"] + str(timestamp) + ".log", filemode='w', format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

log = logging