import datetime

from flask import json
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from pathlib import Path
from messaging import mqtt_publish

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def get_home_controller_events():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(str(Path.home())+ '/creds/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='aj0c1hhtq5fslj8qnqdlp973d8@group.calendar.google.com', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    msg_events = []
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        title = event['summary']
        if ":" in title:
            event_details = title.split(':')
            event_details.append(start)
            msg_events.append(":".join(event_details))

    print (msg_events)
    MQTT_MSG = json.dumps({"name":"|".join(msg_events)})
    mqtt_publish.send("home/calendar/events",MQTT_MSG)
    return None
