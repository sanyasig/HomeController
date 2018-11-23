import datetime
import config_parser
import json
import requests
import ahlogger


def daily(topic=None, details=None):
    config = config_parser.read_config()
    alerts = list(config.items('alerts'))
    now = datetime.datetime.now()
    messages = []

    for x in alerts:
        date = str(x[1])
        event_month = int(int(date.split("/")[1]))
        event_day = int(int(date.split("/")[0]))
        each_message = ""
        message_time = ""

        if (int(now.month) == event_month):

            if (int(now.day) == event_day):
                message_time += "Today"

            if ((int(now.day) + 1) == event_day):
                message_time += "Tomorrow"

        if (message_time != ""):
            message_event = ""
            key = str(x[0])
            message_event += "Its " + key.replace("_", " ") + " " + message_time
            messages.append(message_event)

    if len(messages) > 0:

        for each_message in messages:
            body = json.dumps({
                "notification": each_message,
                "accessCode": config.get('notify_me', 'api_key')
            })
            requests.post(url="https://api.notifymyecho.com/v1/NotifyMe", data=body)
            headers = {"Access-Token": "o.Qiiw4SPAmxx3GbBxZDRO5XpYFcdgtBTq", "Content-Type":"application/json"}
            body = json.dumps({
                "body": each_message,
                "title": 'Travis Reminder'
            })
            requests.post(url="https://api.pushbullet.com/v2/pushes", data=body, headers= headers)

            ACCESS_TOKEN = config.get('push_bullet', 'access_token')
            headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN, 'Content-Type': 'application/json'}
            body = json.dumps({
                'body': each_message,
                'title': 'Travis Reminder',
                'type': 'note'
            })
            response = requests.post(url="https://api.pushbullet.com/v2/pushes", data=body, headers=headers)
            ahlogger.log (response)
            ahlogger.log(each_message)
