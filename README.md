# RaspberryPi Backlight Server

A [Socket.io](https://python-socketio.readthedocs.io/en/latest/index.html) server for controlling an official 7" RaspberryPi Touchscreen Display,
using the [rpi_backlight](https://pypi.org/project/rpi-backlight/) library.

## Installation

1. Install Python

2. Create a virtual environment: `python3 -m venv env` then `source env/Scripts/activate` (or `source env/bin/activate` on Unix)

3. Run `pip3 install -r requirements.txt`

4. Run `python main.py` to start the server!

## Configuration

The default port is [aiohttp](https://docs.aiohttp.org/en/stable/index.html)'s default port, which is 8080. To change it, create a `settings.json`
file in the root of the project, and provide a `port` key with the value of the port that is desired.

For example:

```json
{
    "port": 3000
}
```

## Available Events

- `set_screen_power`: Takes boolean and sets the screen power accordingly

- `get_screen_power`: Returns a boolean indicating the screen power

- `set_brightness`: Takes an integer (or float, which is cast to an int) and sets the brightness accordingly

- `get_brightness`: Returns an integer of the current brightness

- `shutdown`: No arguments, calls `shutdown` on the Pi.
