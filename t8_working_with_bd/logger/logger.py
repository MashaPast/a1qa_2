import logging
import os
import time

timestamp = int(time.time())
logs_dir = os.getcwd() + '/t8_working_with_bd/tests/logs/'

if not os.path.exists(logs_dir):
    os.mkdir(logs_dir)

logging.basicConfig(filename=logs_dir + str(timestamp) + ".log", filemode='w', format='%(asctime)s %(levelname)s '
                                                                                      '%(message)s', level=logging.INFO)

log = logging