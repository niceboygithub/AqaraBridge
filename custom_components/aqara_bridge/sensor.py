import time
from datetime import datetime
from homeassistant.components.sensor import SensorEntity
from .core.utils import local_zone

from .core.aiot_manager import (
    AiotManager,
    AiotEntityBase,
)
from .core.const import (
    BUTTON,
    BUTTON_BOTH,
    CUBE,
    DOMAIN,
    HASS_DATA_AIOT_MANAGER,
    PROP_TO_ATTR_BASE,
    VIBRATION
)

TYPE = "sensor"

DATA_KEY = f"{TYPE}.{DOMAIN}"


async def async_setup_entry(hass, config_entry, async_add_entities):
    manager: AiotManager = hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
    cls_entities = {
        "action": AiotActionSensor,
        "default": AiotSensorEntity
    }
    await manager.async_add_entities(
        config_entry, TYPE, cls_entities, async_add_entities
    )


class AiotSensorEntity(AiotEntityBase, SensorEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotEntityBase.__init__(self, hass, device, res_params, TYPE, channel, **kwargs)
        self._attr_state_class = kwargs.get("state_class")
        self._attr_name = f"{self._attr_name} {self._attr_device_class}"
        self._attr_native_unit_of_measurement = kwargs.get("unit_of_measurement")
        
        tim = round(int(time.time()), 0)
        self._attr_last_update_time = tim
        self._attr_last_update_at = datetime.fromtimestamp(tim, local_zone())
        self._extra_state_attributes.extend(["last_update_time", "last_update_at"])

    @property
    def last_update_time(self):
        self._refresh_data()
        return self._attr_last_update_time

    @property
    def last_update_at(self):
        self._refresh_data()
        return self._attr_last_update_at

    def _refresh_data(self):
        if self.trigger_time is not None:
            self._attr_last_update_time = self.trigger_time
            self._attr_last_update_at = datetime.fromtimestamp(self.trigger_time, local_zone())

    def convert_res_to_attr(self, res_name, res_value):
        if res_name == "battry":
            return int(res_value)
        if res_name == "energy":
            return round(float(res_value) / 1000.0, 3)
        if res_name == "temperature":
            return round(int(res_value) / 100.0, 1)
        if res_name == "humidity":
            return round(int(res_value) / 100.0,1)
        return super().convert_res_to_attr(res_name, res_value)




class AiotActionSensor(AiotSensorEntity, SensorEntity):
    @property
    def icon(self):
        return 'mdi:bell'

    def convert_res_to_attr(self, res_name, res_value):
        if res_name == "firmware_version":
            return res_value
        if res_name == "zigbee_lqi":
            return int(res_value)
        if res_value != 0 and res_value != "" and res_name == "button":
            if res_name == 'vibration' and res_value != '2':
                click_type = VIBRATION.get(res_value, 'unkown')
            if "button" in res_name:
                click_type = BUTTON.get(res_value, 'unkown')

            self.schedule_update_ha_state()
            return click_type
        return super().convert_res_to_attr(res_name, res_value)