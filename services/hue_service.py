from services.parent_service import ParentService
from phue import Bridge

class HueService(ParentService):

    def __init__(self, ip = None):
        self.ip = ip
        self.id = None
        self.bridge = Bridge(self.ip)

    def get_function(self, message=None):
      api = self.bridge.get_api()
      for each_light in api['lights']:
          if(api['lights'][each_light]['name'].lower() == message.get("bulb_name", "none").lower()):
              self.id = each_light

      return self.toggle

    def toggle(self):
        self.bridge.connect()
        curr_state = self.bridge.get_light(int(self.id), 'on')
        if curr_state:
            self.bridge.set_light(int(self.id), 'on', False)
        else:
            self.bridge.set_light(int(self.id), 'on', True)
