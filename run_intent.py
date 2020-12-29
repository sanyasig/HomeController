from services.firestrick_service import FireTv
from services.rmBroadLinkService import RMBroadLInk

if __name__ == "__main__":
   a = RMBroadLInk()
   a.toggle_power()
   pass

  # services = RMBroadLInk(ip="192.168.0.17")
   #services.toggle_power()
  # services.clear_tracklist(
   #ervices.turn_on_bt_audio()



   # button_name = "andex"
   # MQTT_MSG = json.dumps({"name": button_name, "bulb_name": "bedroom"})
   #
   # print(platform.python_version())
   # service = HueService('192.168.0.10')
   # message = {}
   # message['name'] = 'kitchen'
   # value = service.get_function(message)
   # value()