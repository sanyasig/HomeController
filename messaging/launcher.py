import paho.mqtt.client as mqtt
import json
import ahlogger

from messaging.messager_processor import process_message


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
        ahlogger.log(("message received " ,str(message.payload.decode("utf-8"))))
        ahlogger.log(("message topic=",message.topic))
        ahlogger.log(("message qos=",message.qos))
        ahlogger.log(("message retain flag=",message.retain))
        process_message(message.topic, message.payload)

    def on_connect(self, client, userdata, flags, rc):
        ahlogger.log(("Connected with result code " + str(rc)))
        ahlogger.log("subscribing to home/#")
        client.subscribe("home/#")

def start_process(ip= None):
    messager = HomeMessager(ip)
    messager.launch()