from services.firestrick_service import FireStick
from services.rmBroadLinkService import RMBroadLInk
import time
import  json
import ahlogger

def kodi(topic=None, details=None):
    ## turm on tv
    RMBroadLInk().toggle_power()
    time.sleep(10)
    FireStick().turn_on_kodi()
    ahlogger.log ("in tv platform")

def youtube(topic=None, details=None):
    ## turm on tv
    RMBroadLInk().toggle_power()
    time.sleep(10)
    FireStick().turn_on_kodi()
    ahlogger.log ("in tv platform")

def itself(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    RMBroadLInk(ip).toggle_power()
