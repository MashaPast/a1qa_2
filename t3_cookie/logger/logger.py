import logging
from t3_cookie.helpers.helpers import Loader
import time

timestamp = int(time.time())

CONFIG_DATA = Loader.get_config()

logging.basicConfig(filename=CONFIG_DATA["LOG_DIR"] + str(timestamp) + ".log", filemode='w', format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

log = logging

