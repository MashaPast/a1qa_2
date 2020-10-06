import configparser
from os.path import abspath

config = configparser.ConfigParser()
config.read(abspath("./t8_working_with_bd/resources/config_db.ini"))