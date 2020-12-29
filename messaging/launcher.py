import paho.mqtt.client as mqtt
import json
import logging

from services.firestrick_service import FireTv
from services.rmBroadLinkService import RMBroadLInk


class HomeMessager():

    pi_ip = None

    def __init__(self, ip = None):
        self.pi_ip = ip

    def launch(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(self.pi_ip)
        client.loop_forever()

    def on_message(self, client, userdata, message):
        logging.info("message received " ,str(message.payload.decode("utf-8")))
        logging.info(("message topic=",message.topic))
        logging.info(("message qos=",message.qos))
        logging.info(("message retain flag=",message.retain))
        process_message(message.topic, message.payload)

    def on_connect(self, client, userdata, flags, rc):
        logging.info(("Connected with result code " + str(rc)))
        logging.info("subscribing to home/#")
        client.subscribe("home/#")


def start_process(ip= None):
    messager = HomeMessager(ip)
    messager.launch()


def process_message(topic=None, message=None):
    # TODO: need to fix the dynamic loading of modules
    try:
        print("topic: " + topic)
        print("status " + str(message))

        services = {
            'firetv': FireTv(),
            'tv': RMBroadLInk(),
            }
        intent = topic.split('/')[1]
        module = services[intent]
        logging.info("calling module " + str(module))
        func = getattr(module, topic.split("/")[2])
        func(topic, message)
    except :
        logging.info("cannot find service")