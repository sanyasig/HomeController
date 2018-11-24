import json
import requests
import logging

def playlist(topic=None, details=None):
    ip = None
    all_details = json.loads(details)

    ip = all_details.get('ip')
    name = all_details.get('playlist')

    url = "http://" +str(ip) + "/api/v1/commands/?cmd=playplaylist&name=" + str(name)
    logging.info(url)
    r = requests.get(url)
    logging.info(r.status_code)

    logging.info("")
