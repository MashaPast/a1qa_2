import logging
from t5_userinyerface import CONFIG_DATA
import time

timestamp = int(time.time())

logging.basicConfig(filename=CONFIG_DATA["LOG_DIR"] + str(timestamp) + ".log", filemode='w', format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

log = logging