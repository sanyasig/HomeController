from services.rmBroadLinkService import RMBroadLInk


def tv_audio(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    if(details.decode("utf-8") =='ON'):
        RMBroadLInk(ip).turn_on_tv_audio()

def bt_audio(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    if (details.decode("utf-8") == 'ON'):
        RMBroadLInk(ip).turn_on_bt_audio()
