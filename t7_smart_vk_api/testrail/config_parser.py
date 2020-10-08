import configparser
from os.path import abspath

config = configparser.ConfigParser()
config.read(abspath("./t7_smart_vk_api/testrail/config_testrail.ini"))

