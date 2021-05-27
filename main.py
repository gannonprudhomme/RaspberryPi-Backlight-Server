import logging
import os
import json
from aiohttp import web
import socketio
from commands import RaspberryPi
from base_logger import setup_logging

CONFIG_FILE_NAME = "settings.json"
DEFAULT_PORT = 8080

setup_logging()
rpi = RaspberryPi()
sio = socketio.AsyncServer(async_mode='aiohttp')

@sio.on('shutdown')
def shutdown(_, __):
    """ Receives shutdown event and calls shutdown on the Pi """
    logging.info('shutdown')
    rpi.shutdown()

@sio.on('set_screen_power')
def set_screen_power(_, data):
    """ Retrieves event and sets the given Pi screen power value """
    if isinstance(data, bool):
        logging.info('set_screen_power %s', str(data))
        rpi.set_screen_power(data)
    else:
        logging.warning('set_screen_power w/ invalid value! %s', str(data))

@sio.on('get_screen_power')
def get_screen_power(_, __):
    """ Retrieves event and returns the corresponding Pi screen power value """
    value = rpi.get_screen_power()
    logging.info('get_screen_power %s', str(value))
    return value

@sio.on('set_brightness')
def set_brightness(_, data):
    """ Receives set_brightness command and sets it on the Pi screen """
    if data is not None and isinstance(data, int) or isinstance(data, float):
        data = int(data)
        logging.info('set_brightness %d', data)
        rpi.set_brightness(data)
    else:
        logging.warning('set_brightness w/ invalid value! %s', str(data))

@sio.on('get_brightness')
def get_brightness(_, __):
    """ Receives get_brightness event and returns the corresponding brightness """
    brightness = rpi.get_brightness()

    logging.info('get_brightness %d', brightness)

    return brightness

@sio.event
def connect(_, data, __):
    """ Handles connect event """
    addr = data.get('REMOTE_ADDR')
    logging.info('Connection from %s', addr)

def main():
    """ Entrypoint of the program """
    app = web.Application()

    config_file = os.path.dirname(__file__) + f"./{CONFIG_FILE_NAME}"
    port = DEFAULT_PORT

    try:
        with open(config_file, "r") as config:
            json_port = json.load(config).get("port")
            if json_port:
                port = int(json_port)
                logging.info("Config file '%s' loaded successfully with port '%d'",
                             CONFIG_FILE_NAME, port)
            else:
                logging.warning("Config file '%s' was loaded, but port was invalid: %s",
                                CONFIG_FILE_NAME, str(json_port))
    except FileNotFoundError:
        logging.warning("Config file '%s' not found! Using default port of %d",
                        CONFIG_FILE_NAME, DEFAULT_PORT)

    sio.attach(app)
    web.run_app(app, port=port)

if __name__ == '__main__':
    main()
