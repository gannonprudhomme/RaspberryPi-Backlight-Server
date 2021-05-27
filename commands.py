from rpi_backlight import Backlight

ON_PI = False

class RaspberryPi():
    def __init__(self):
        # If we're a raspberry pi
        self.backlight = None
        if ON_PI:
            self.backlight = Backlight()

    def shutdown(self):
        """ Shutdown the Pi """
        # Idk what we do here
        pass

    def sleep(self):
        """ Make the screen sleep and wake on touch """
        if not self.backlight:
            return

        backlight.power = False

    def set_brightness(self, brightness: int):
        """ Set the brightness to the given value """
        if not self.backlight:
            return

        if self.backlight < 0 or self.backlight > 100:
            # Print an error, probably
            return
        
        self.backlight.brightness = brightness

    def get_brightness(self) -> int:
        """ Retrieve the brightness """
        if not self.backlight:
            return -1
        
        return self.backlight.brightness