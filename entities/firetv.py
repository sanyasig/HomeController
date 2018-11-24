from services.firestrick_service import FireStick
import json
from multiprocessing import Pool, Process

def restart(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    stick = FireStick(ip)
    p = Process(target=stick.restart(), args=())
    p.start()
    p.join()

def kodi(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    stick = FireStick(ip)
    p = Process(target=stick.turn_on_kodi(), args=())
    p.start()
    p.join()

def youtube(topic=None, details=None):
    ip = str(topic).split("/")[-1]
    stick = FireStick(ip)
    p = Process(target=stick.turn_on_youtube(), args=())
    p.start()
    p.join()