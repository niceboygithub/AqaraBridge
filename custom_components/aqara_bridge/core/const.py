"""Constants for the Aqara Bridge component."""
DOMAIN = "aqara_bridge"

# Config flow fields
CONF_FIELD_ACCOUNT = "field_account"
CONF_FIELD_COUNTRY_CODE = "field_country_code"
CONF_FIELD_AUTH_CODE = "field_auth_code"
CONF_FIELD_SELECTED_DEVICES = "field_selected_devices"
CONF_FIELD_REFRESH_TOKEN = "field_refresh_token"
CONF_FIELD_APP_ID = "field_app_id"
CONF_FIELD_APP_KEY = "field_app_key"
CONF_FIELD_KEY_ID = "field_key_id"
CONF_OCCUPANCY_TIMEOUT = 'occupancy_timeout'

# Cloud
SERVER_COUNTRY_CODES = ["CN", "USA", "KR", "RU", "GER"]
SERVER_COUNTRY_CODES_DEFAULT = "CN"
DEFAULT_CLOUD_APP_ID = "88110776288481280040ace0"
DEFAULT_CLOUD_APP_KEY = "t7g6qhx4nmbeqmfq1w6yksucnbrofsgs"
DEFAULT_CLOUD_KEY_ID = "K.881107763014836224"

# CONFIG ENTRY
CONF_ENTRY_APP_ID = "app_id"
CONF_ENTRY_APP_KEY = "app_key"
CONF_ENTRY_KEY_ID = "key_id"
CONF_ENTRY_AUTH_ACCOUNT = "account"
CONF_ENTRY_AUTH_ACCOUNT_TYPE = "account_type"
CONF_ENTRY_AUTH_COUNTRY_CODE = "country_code"
CONF_ENTRY_AUTH_EXPIRES_IN = "expires_in"
CONF_ENTRY_AUTH_EXPIRES_TIME = "expires_datetime"
CONF_ENTRY_AUTH_ACCESS_TOKEN = "access_token"
CONF_ENTRY_AUTH_REFRESH_TOKEN = "refresh_token"
CONF_ENTRY_AUTH_OPENID = "open_id"

# HASS DATA
HASS_DATA_AUTH_ENTRY_ID = "auth_entry_id"
HASS_DATA_AIOTCLOUD = "aiotcloud"
HASS_DATA_AIOT_MANAGER = "aiot_manager"

ATTR_FIRMWARE_VERSION = "firmware_version"
ATTR_ZIGBEE_LQI = "zigbee_lqi"
ATTR_VOLTAGE = "voltage"


PROP_TO_ATTR_BASE = {
    "firmware_version": ATTR_FIRMWARE_VERSION,
    "zigbee_lqi": ATTR_ZIGBEE_LQI,
    "voltage": ATTR_VOLTAGE
}

# Air Quality Monitor
ATTR_CO2E = "carbon_dioxide_equivalent"
ATTR_TVOC = "total_volatile_organic_compounds"
ATTR_HUMIDITY = "humidity"

# Switch Sensor
# https://github.com/Koenkk/zigbee-herdsman-converters/blob/master/converters/fromZigbee.js#L4738
BUTTON = {
    '1': 'single',
    '2': 'double',
    '3': 'triple',
    '4': 'quadruple',
    '16': 'hold',
    '17': 'release',
    '18': 'shake',
    '20': 'reversing_rotate',
    '21': 'hold_rotate',
    '22': 'clockwise',
    '23': 'counterclockwise',
    '24': 'hold_clockwise',
    '25': 'hold_counterclockwise',
    '26': 'rotate',
    '27': 'hold_rotate',
    '128': 'many'
}

BUTTON_BOTH = {
    '4': 'single',
    '5': 'double',
    '6': 'triple',
    '16': 'hold',
    '17': 'release',
}

VIBRATION = {
    '1': 'vibration',
    '2': 'tilt',
    '3': 'drop',
}

CUBE = {
    '0': 'flip90',
    '1': 'flip180',
    '2': 'move',
    '3': 'knock',
    '4': 'quadruple',
    '16': 'rotate',
    '20': 'shock',
    '28': 'hold',
    'move': 'move',
    'flip90': 'flip90',
    'flip180': 'flip180',
    'rotate': 'rotate',
    'alert': 'alert',
    'shake_air': 'shock',
    'tap_twice': 'knock'
}
