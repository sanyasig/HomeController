from lifxlan import LifxLAN

from services.parent_service import ParentService


class LifxService(ParentService):

    def __init__(self):
        self.bulb = None

    def get_function(self, message=None):

        lifx = LifxLAN(1)
        devices = lifx.get_lights()
        mac = message.get("mac", "none")
        for each_buld in devices:
            print (each_buld.mac_addr)
            if each_buld.mac_addr == mac:
                self.bulb = each_buld
        return self.toggle


    def toggle(self):
        original_power_state = self.bulb.get_power()
        if(original_power_state == 0):
            self.bulb.set_power(power=True)
        else:
            self.bulb.set_power(power=False)
