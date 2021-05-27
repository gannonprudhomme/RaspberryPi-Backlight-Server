import logging
from aiohttp import web
import socketio
from commands import RaspberryPi

sio = socketio.AsyncServer(async_mode='aiohttp')

rpi = RaspberryPi()

logging.basicConfig(format='%(levelname)s %(asctime)s: %(message)s',
                    datefmt='%I:%M:%S %p', filename='logs.log')
_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)

@sio.on('shutdown')
def shutdown(sid, data):
    _LOGGER.info('shutdown')
    rpi.shutdown()

@sio.on('sleep')
def sleep(sid, data):
    _LOGGER.info('sleep')
    rpi.sleep()

@sio.on('set_brightness')
def set_brightness(sid, data):
    # Attempt to get the brightness from data
    print(data)
    pass

@sio.on('get_brightness')
def get_brightness(sid, data):
    brightness = rpi.get_brightness()

    _LOGGER.info('get_brightness %d', brightness)

    return brightness

@sio.event
def connect(sid, data, _):
    addr = data.get('REMOTE_ADDR')
    _LOGGER.info('Connection from %s', addr)

if __name__ == '__main__':
    app = web.Application()

    sio.attach(app)
    web.run_app(app)