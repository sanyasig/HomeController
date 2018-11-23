from services.parent_service import ParentService
from . import Utils
import ahlogger

class Home_PC(ParentService):

    shutdown_cmd = "sudo ./scripts/shutdown.sh"

    def __init__(self, ip=None, username=None, password=None):
        self.ip = ip
        self.username = username
        self.password = password


    def get_function(self, message=None):

        split_message = message.split("_")
        return_fuction = None

        if len(split_message) > 1:
            if (split_message[1] == "self"):
                if split_message[2] == "shutdown":
                    return_fuction = self.shutdown
        return  return_fuction


    def shutdown(self):
        output = Utils.execute_remote_command(self.ip, self.username, self.password, self.shutdown_cmd)
        ahlogger.log(output)

