import requests

import config_parser
import ahlogger


def trigger(topic=None, details=None):
    key = config_parser.read_config().get('ifttt', 'key')
    url = "https://maker.ifttt.com/trigger/" + str(details) +"/with/key/" + str(key)
    ahlogger.log(url)
    r = requests.post(url)
    ahlogger.log(r.status_code)




