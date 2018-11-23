from services.firestrick_service import FireStick
from services.pc_service import Home_PC
import configparser
import  os

from services.rmBroadLinkService import RMBroadLInk
import ahlogger


def getService(topic):

     if("adb" in topic):
         return FireStick("192.168.0.17")

     if ("tv" in topic):
         return RMBroadLInk("192.168.0.17")

     elif("pc" in topic):
         config = get_config("pc")
         return Home_PC(config.get("Host"), config.get("User"), config.get("Passwd"))

def read_config():
    config = configparser.ConfigParser()
    ahlogger.log((config.sections()))
    config.read(os.path.expanduser('~') + '/work/alexa_settings.ini')
    return config

def get_config(type):
    config = read_config()
    return {
     'youtube': config['youtube'],
     'b': 2,
     'pc': config['pc'],
    }[type]


# def execute_remote_command(hostname=None, username=None, password=None, command=None):
#     port = 22
#     output = None
#
#     try:
#         client = paramiko.SSHClient()
#         client.load_system_host_keys()
#         client.set_missing_host_key_policy(paramiko.WarningPolicy)
#
#         client.connect(hostname, port=port, username=username, password=password)
#
#         stdin, stdout, stderr = client.exec_command(command)
#         ahlogger.log stdout.read(),
#
#     finally:
#         client.close()

