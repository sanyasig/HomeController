import broadlink
import time

from services.parent_service import ParentService
import ahlogger

class RMBroadLInk(ParentService):

    def __init__(self, ip = None):
        self.ip = ip

    def get_function(self, message=None):
        split_message = message.split("_")
        return_fuction = None
        if len(split_message) > 1:
            if (split_message[1] == "tv"):
                if split_message[2] == "on":
                    ahlogger.log("turing on TV")
                    return_fuction = self.toggle_power
                else:
                    ahlogger.log("turing off youtube")
                    return_fuction = self.toggle_power

        return return_fuction

    def toggle_power(self):
        device = self._connect_if_rm()
        codeData = "26008c009694133713371436141213121312131213121337133713371312141114111412131213121337131213121312131213121312133714111436143713371337133713371300060d949611391139113a111411141114111411141139113911391114111510151114111411141139111411141114111411141213113a1015103a1139113911391139113911000d05000000000000000000000000"
        self._send_code(device=device, codeData=codeData)

    def turn_on_bt_audio(self):
        device = self._connect_if_rm()
        codeData1 = "2600580000012a95121313371213133712391238123911141337121313371412131213121312133713121312131313121337121313121312133713381337123913121337133713381100052000012a4a12000c600001294b12000d05"
        codeData2 = "260050000001289613121337121413371238133811391213133713121338111413121312131212381312133813121337133714121312131213371213143712131312133813371337120005210001294a12000d050000000000000000"
        self._send_code(device=device, codeData=codeData1)
        time.sleep(1)
        self._send_code(device=device,codeData=codeData2)


    def turn_on_tv_audio(self):
        device = self._connect_if_rm()
        codeData1 = "2600580000012a95121313371213133712391238123911141337121313371412131213121312133713121312131313121337121313121312133713381337123913121337133713381100052000012a4a12000c600001294b12000d05"
        codeData2 = "260054000d00049a00012995111413371213133712381239123812131337131213371213121313121312133713371338131213371337121313121213131213121337131213121337133713381300051c0001284b13000d0500000000"
        self._send_code(device=device, codeData=codeData1)
        time.sleep(1)
        self._send_code(device=device, codeData=codeData2)

    def _connect_if_rm(self):
        device = broadlink.rm(host=(self.ip, 80), mac=bytearray.fromhex("34ea344298bf"))
        ahlogger.log("Connecting to Broadlink device....")
        device.auth()
        time.sleep(1)
        ahlogger.log("Connected....")
        time.sleep(1)
        device.host
        return device

    def _send_code(self, device=None, codeData=None):
        bytes.fromhex(codeData)
        device.send_data(bytes.fromhex(codeData))

