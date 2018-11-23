import subprocess
import time
from multiprocessing import Pool, Process

from services.parent_service import ParentService


class FireStick(ParentService):

    stop_kodi="adb shell am force-stop org.xbmc.kodi"
    start_kodi="adb shell am start -n org.xbmc.kodi/.Splash"
    start_youtube="adb shell am start -n org.chromium.youtube_apk/.YouTubeActivity"
    stop_youtube="adb shell am force-stop org.chromium.youtube_apk"

    def __init__(self, ip = None):
        self.ip = ip

    def get_function(self, message=None):

        split_message = message.split("_")
        return_fuction = None

        if len(split_message) > 1:
            if (split_message[1] == "youtube"):
                if split_message[2] == "on":
                    print("turing on youtube")
                    return_fuction =  self.turn_on_youtube
                else:
                    print("turing off youtube")
                    return_fuction = self.turn_off_youtube

            elif (split_message[1] == "kodi"):
                if split_message[2] == "on":
                    print("turing on kodi")
                    return_fuction = self.turn_on_kodi
                else:
                    print("turing off kodi")
                    funtion = self.turn_off_kodi
            elif (split_message[1] == "self"):
                return_fuction = self.restart
        return return_fuction

    def restart(self):
        self.reconnect()
        output, error = self.run_bash_command("adb reboot")
        self.dissconnect()
        print("stuff")

    def turn_on_youtube(self):
        self.reconnect()
        self.run_bash_command(self.stop_kodi)
        self.run_bash_command("sleep 1")
        self.run_bash_command(self.start_youtube)
        self.run_bash_command("adb shell input keyevent 25")
        self.dissconnect()

    def turn_off_youtube(self):
        self.reconnect()
        self.run_bash_command(self.stop_youtube)
        self.run_bash_command("adb shell input keyevent 25")
        self.dissconnect()

    def turn_on_kodi(self):
        self.reconnect()
        self.run_bash_command(self.stop_youtube)
        self.run_bash_command(self.start_kodi)
        self.run_bash_command("adb shell input keyevent 25")
        self.dissconnect()

    def turn_off_kodi(self):
        self.reconnect()
        self.run_bash_command(self.stop_kodi)
        self.run_bash_command("adb shell input keyevent 25")
        self.dissconnect()

    def run_bash_command(self, bashCommand):
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        time.sleep(1)
        print(output)

    def reconnect(self):
        self.run_bash_command("adb kill-server")
        self.run_bash_command("adb start-server")
        self.run_bash_command("adb connect " + self.ip)

    def dissconnect(self):
        self.run_bash_command("adb kill-server")

