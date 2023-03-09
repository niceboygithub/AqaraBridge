import time
from datetime import datetime
from homeassistant.components.sensor import SensorEntity
from .core.utils import local_zone

from .core.aiot_manager import (
    AiotManager,
    AiotEntityBase,
)
from .core.const import (
    DOMAIN,
    HASS_DATA_AIOT_MANAGER,
)

TYPE = "sensor"

DATA_KEY = f"{TYPE}.{DOMAIN}"


async def async_setup_entry(hass, config_entry, async_add_entities):
    manager: AiotManager = hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
    cls_entities = {
        "default": AiotSensorEntity
    }
    await manager.async_add_entities(
        config_entry, TYPE, cls_entities, async_add_entities
    )


class AiotSensorEntity(AiotEntityBase, SensorEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotEntityBase.__init__(self, hass, device, res_params, TYPE, channel, **kwargs)
        self._attr_state_class = kwargs.get("state_class")
        self._attr_native_unit_of_measurement = kwargs.get("unit_of_measurement")
        self._extra_state_attributes.extend(["last_update_time", "last_update_at"])

    @property
    def last_update_time(self):
        return self.trigger_time

    @property
    def last_update_at(self):
        return self.trigger_dt

    def convert_res_to_attr(self, res_name, res_value):
        if res_name == "battry":
            return int(res_value)
        if res_name == "rotation_angle":
            return int(res_value)
        if res_name == "press_rotation_angle":
            return int(res_value)
        if res_name == "energy":
            return round(float(res_value) / 1000.0, 3)
        if res_name == "temperature":
            return round(int(res_value) / 100.0, 1)
        if res_name == "humidity":
            return round(int(res_value) / 100.0,1)
        return super().convert_res_to_attr(res_name, res_value)