import os
from rpi_backlight import Backlight
from base_logger import logger

# Set this to True when testing (e.g. on a Windows computer)
DEBUG = False

def get_serial_number() -> str:
    """ Get the serial number from the Pi
        Source: https://raspberrypi.stackexchange.com/a/2087
    """
    cpuserial = "0000000000000000"
    try:
        with open('/proc/cpuinfo', 'r') as file:
            for line in file:
                if line[0:6]=='Serial':
                    cpuserial = line[10:26]
    except FileNotFoundError:
        cpuserial = "ERROR000000000"
        logger.error("Cannot get serial number")

    return cpuserial

def get_model() -> str:
    """ Get the model of the Pi """
    ret = None
    try:
        with open('/proc/device-tree/model') as file:
            for line in file:
                ret = line
    except FileNotFoundError:
        logger.error("Cannot get device model")

    return ret

class RaspberryPi():
    """ Handles RaspberryPi state & commands """
    def __init__(self):
        # If we're a raspberry pi
        self.backlight = None
        if DEBUG:
            self.backlight = Backlight(":emulator:")
        else:
            try:
                self.backlight = Backlight()
            except FileNotFoundError as err:
                logger.error(err)
                logger.error('You should probably be running with DEBUG=True')

    def get_device_info(self): # pylint: disable=no-self-use
        """ Returns the serial number and model of the Pi """
        serial = get_serial_number()
        model = get_model()

        return {
            "serial": serial,
            "model": model,
        }

    def shutdown(self):
        """ Shutdown the Pi """
        if not self.backlight:
            return

        os.system("shutdown now")

    def sleep(self):
        """ Make the screen sleep and wake on touch """
        if not self.backlight:
            return

        self.backlight.power = False

    def set_power(self, power: bool):
        """ Sets the backlight screen power """
        if not self.backlight:
            return

        self.backlight.power = power

    def get_power(self) -> bool:
        """ Retrieves the backlight screen power """
        if not self.backlight:
            return None

        return self.backlight.power

    def set_brightness(self, brightness: int):
        """ Set the brightness to the given value """
        if not self.backlight:
            return

        if brightness < 0 or brightness > 100:
            # Print an error, probably
            return

        self.backlight.brightness = brightness

    def get_brightness(self) -> int:
        """ Retrieve the backlight brightness """
        if not self.backlight:
            return -1

        return self.backlight.brightness
