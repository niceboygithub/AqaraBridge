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

TYPE = "button"

DATA_KEY = f"{TYPE}.{DOMAIN}"


async def async_setup_entry(hass, config_entry, async_add_entities):
    manager: AiotManager = hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
    cls_entities = {
        "default": AiotButtonEntity
    }
    await manager.async_add_entities(
        config_entry, TYPE, cls_entities, async_add_entities
    )


class AiotButtonEntity(AiotEntityBase, SensorEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotEntityBase.__init__(self, hass, device, res_params, TYPE, channel, **kwargs)
        self._attr_state_class = kwargs.get("state_class")
        self._attr_name = f"{self._attr_name} {self._attr_device_class}"
        self._attr_press_type = None

        self._attr_last_update_time = None
        self._attr_last_update_at = None
        self._extra_state_attributes.extend(["press_type", "trigger_time", "trigger_dt"])
        
    @property
    def native_value(self):
        if self.trigger_time is not None:
            return datetime.fromtimestamp(self.trigger_time, local_zone(self.hass))
        else:
            return datetime.fromtimestamp(time.time(), local_zone(self.hass))

    @property
    def press_type(self):
        return self._attr_press_type

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
