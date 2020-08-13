import logging
from t2_modal_windows.helpers.helpers import get_config_data

CONFIG_DATA = get_config_data()

logging.basicConfig(filename=CONFIG_DATA["LOG_FILE"], filemode='w', format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

appLogger = logging
