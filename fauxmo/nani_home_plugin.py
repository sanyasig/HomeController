import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from typing import Union  # noqa
from paho.mqtt.client import Client, MQTTMessage
from fauxmo.plugins import FauxmoPlugin


class RESTAPIPlugin(FauxmoPlugin):
    """REST API plugin class.

    The Fauxmo class expects plugins to be instances of objects that have on()
    and off() methods that return True on success and False otherwise. This
    class takes a mix of url, method, header, body, and auth data and makes
    REST calls to a device.
    """

    def __init__(
            self,
            *,
            auth_type: str = None,
            headers: dict = None,
            method: str = "GET",
            name: str,
            off_cmd: str,
            off_data: dict = None,
            off_json: dict = None,
            on_cmd: str,
            on_data: dict = None,
            on_json: dict = None,
            password: str = None,
            port: int,
            state_cmd: str = None,
            state_data: dict = None,
            state_json: dict = None,
            state_method: str = "GET",
            state_response_off: str = None,
            state_response_on: str = None,
            user: str = None,
            mqtt_server: str = "192.166.1.11",
            mqtt_port: int = 1883,


    ) -> None:
        """Initialize a RESTAPIPlugin instance.

        Args:
            auth_type: Either `basic` or `digest` if needed
            headers: Additional headers for both `on()` and `off()`
            method: HTTP method to be used for both `on()` and `off()`
            off_cmd: URL to be called when turning device off
            off_data: HTTP body to turn device off
            off_json: JSON body to turn device off
            on_cmd: URL to be called when turning device on
            on_data: HTTP body to turn device on
            on_json: JSON body to turn device on
            password: Password for `auth`
            state_cmd: URL to be called to determine device state
            state_data: Optional POST data to query device state
            state_json: Optional json data to query device state
            state_method: HTTP method to be used for `get_state()`
            state_response_off: If this string is in the response to state_cmd,
                                the device is off.
            state_response_on: If this string is in the response to state_cmd,
                               the device is on.
            user: Username for `auth`
        """
        self.method = method
        self.state_method = state_method
        self.headers = headers
        self.auth: Union[HTTPBasicAuth, HTTPDigestAuth] = None

        self.on_cmd = on_cmd
        self.off_cmd = off_cmd
        self.state_cmd = state_cmd

        self.on_data = on_data
        self.off_data = off_data
        self.state_data = state_data

        self.on_json = on_json
        self.off_json = off_json
        self.state_json = state_json
        self.client = Client()
        self.client.connect(mqtt_server, mqtt_port, 60)

        self.state_response_on = state_response_on
        self.state_response_off = state_response_off
        self.state = 'on'

        if auth_type:
            if auth_type.lower() == "basic":
                self.auth = HTTPBasicAuth(user, password)

            elif auth_type.lower() == "digest":
                self.auth = HTTPDigestAuth(user, password)

        super().__init__(name=name, port=port)

    def _publish(self, topic: str, value: str) -> bool:
        msg = self.client.publish(topic, value)
        try:
            msg.wait_for_publish()
        except ValueError:
            return False
        return True

    def get_toggeled_state(self, curr_state):
        new_state = 'off'
        if self.state == "off":
            new_state = 'on'
        return new_state

    def on(self) -> bool:
        """Turn device on."""
        print(self.on_cmd)
        self._publish(self.on_cmd, 'DUMMY')
        return self.set_state(self.on_cmd, self.on_data, self.on_json)

    def off(self) -> bool:
        """Turn device off."""
        self._publish(self.off_cmd, 'DUMMY')
        return self.set_state(self.off_cmd, self.off_data, self.off_json)

    def set_state(self, cmd: str, data: dict, json: dict) -> bool:
        self.state = self.get_toggeled_state(self.state)
        return True

    def get_state(self) -> str:
        return self.state