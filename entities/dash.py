import json
from services.hue_service import HueService

def button_press(topic=None, details=None):
    service = HueService('192.168.0.10')
    message = json.loads(details.decode('utf8'))
    value = service.get_function(message)
    value()
