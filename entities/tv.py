from services.Utils import print_name
from services.firestrick_service import FireTv
from services.rmBroadLinkService import RMBroadLInk


@print_name
def itself(topic=None, details=None):
    action = topic.split("/")[3]
    if action == 'toggle_power':
        RMBroadLInk().toggle_power()


@print_name
def firetv(topic=None, details=None):
    action = topic.split("/")[3]
    fire_tv_service = FireTv()
    if action == "start_kodi":
        fire_tv_service.start_kodi()
    if action == "stop_kodi":
        fire_tv_service.kill_kodi()
    if action == "restart":
        fire_tv_service.firerv_restart()
