"""Consts used by NHC2."""
from homeassistant.const import CONF_HOST  # noqa pylint: disable=unused-import

DOMAIN = 'nhc2'
KEY_GATEWAY = 'nhc2_gateway'
BRAND = 'Niko'
LIGHT = 'Light'
SWITCH = 'Switch'
COVER = 'Cover'
FAN = 'Fan'
CLIMATE = 'Thermostat'
ENERGY = 'CentralMeter'
BUTTON = 'Button'
CONF_SWITCHES_AS_LIGHTS = 'switches_as_lights'
DEFAULT_PORT = 8883
KEY_MANUAL = 'MANUAL_IP_HOST'

ROLL_DOWN_SHUTTER = 'rolldownshutter'
SUN_BLIND = 'sunblind'
GATE = 'gate'
VENETIAN_BLIND = 'venetianblind'
GARAGE_DOOR = 'garagedoor'

SERVICE_SET_LIGHT_BRIGHTNESS = 'set_light_brightness'

ATTR_LIGHT_BRIGHTNESS = 'light_brightness'
