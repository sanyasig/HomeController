import configparser
import logging
import os
from functools import wraps


def read_config():
    config = configparser.ConfigParser()
    logging.info((config.sections()))
    config.read(os.path.expanduser('~') + '/work/alexa_settings.ini')
    return config


def get_config(type):
    config = read_config()
    return {
     'youtube': config['youtube'],
     'b': 2,
     'pc': config['pc'],
    }[type]


def print_name(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("calling INTENT {} and function {}".format(__name__, f.__name__))
        print(args[0])
        return f(*args, **kwargs)
    return wrapper