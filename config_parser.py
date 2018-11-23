import configparser
import  os

import ahlogger

config = 0;

def read_config():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~') + '/home_settings.ini')
    ahlogger.log(config.sections())
    return config


def get_config(type):
    config = read_config()
    return {
        'youtube': config['youtube'],
        'b': 2,
        'pc' : config['pc'],
    }[type]
