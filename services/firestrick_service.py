import subprocess
import time
from services.HomeService import HomeService

START_YOUTUBE = ""
STOP_KODI = "adb shell am force-stop org.xbmc.kodi"
START_KODI = "adb shell am start -n org.xbmc.kodi/.Splash"
key = "adb shell input keyevent 25"


class FireTv(HomeService):

    def __init__(self):
        firetv_config = self.get_config('firetv')
        self.ip = firetv_config['ip']
        self.port = firetv_config['port']

    def start_kodi(self):
        self.run_intent(START_KODI)

    def kill_kodi(self):
        self.run_intent(STOP_KODI)

    def firerv_restart(self):
        self.run_intent("adb reboot")

    def run_intent(self, intent_str):
        if self.check_connected():
            self.run_bash_cmd(intent_str)

    def check_connected(self, re_connect=True):
        response = self.run_bash_cmd('adb devices')
        if self.ip in response:
            return True
        else:
            self.run_bash_cmd("adb kill-server")
            time.sleep(1)
            self.run_bash_cmd("adb start-server")
            time.sleep(1)
            second_resp = self.run_bash_cmd("adb connect " + self.ip)
            time.sleep(1)
            if self.ip in second_resp:
                return True
            return False

    def run_bash_cmd(self, command):
        p1 = subprocess.Popen(command, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        response = str(p1.communicate())
        return response

