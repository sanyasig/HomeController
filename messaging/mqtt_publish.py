
import paho.mqtt.publish as publish

import ahlogger


def send(topic, message):
    ahlogger.log("sending " +message + " to " + topic)
    publish.single(topic, message, hostname="192.168.0.14")

