import os
from rpi_backlight import Backlight
from base_logger import logger

# Set this to True when testing (e.g. on a Windows computer)
DEBUG = False

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
