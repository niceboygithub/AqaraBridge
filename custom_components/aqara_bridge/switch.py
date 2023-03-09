from homeassistant.components.switch import SwitchEntity

from .core.aiot_manager import AiotManager, AiotToggleableEntityBase
from .core.const import DOMAIN, HASS_DATA_AIOT_MANAGER, PROP_TO_ATTR_BASE

TYPE = "switch"

DATA_KEY = f"{TYPE}.{DOMAIN}"

async def async_setup_entry(hass, config_entry, async_add_entities):
    manager: AiotManager = hass.data[DOMAIN][HASS_DATA_AIOT_MANAGER]
    cls_entities = {
        "default": AiotSwitchEntity,
        "wall_switch": AiotWallSwitchEntity
    }
    await manager.async_add_entities(
        config_entry, TYPE, cls_entities, async_add_entities
    )

DISABLE_MAPPING = {
    "4.1.85" : "4.10.85",
    "4.2.85" : "4.11.85",
    "4.3.85" : "4.12.85",
}

class AiotSwitchEntity(AiotToggleableEntityBase, SwitchEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotToggleableEntityBase.__init__(
            self, hass, device, res_params, TYPE, channel, **kwargs
        )
        self._extra_state_attributes.extend([])

    @property
    def icon(self):
        """return icon."""
        return 'mdi:power-socket'

    def convert_res_to_attr(self, res_name, res_value):
        if res_name == "toggle" or res_name == "decoupled":
            return res_value == "1"
        if res_name == "energy":
            return round(float(res_value) / 1000.0, 3)
        if res_name == "firmware_version":
            return res_value
        if res_name == "zigbee_lqi":
            return int(res_value)
        if res_name == "in_use":
            return res_value == "1"
        return super().convert_res_to_attr(res_name, res_value)


class AiotWallSwitchEntity(AiotToggleableEntityBase, SwitchEntity):
    def __init__(self, hass, device, res_params, channel=None, **kwargs):
        AiotToggleableEntityBase.__init__(
            self, hass, device, res_params, TYPE, channel, **kwargs
        )
        self._attr_disable_btn = None
        self._extra_state_attributes.extend(["trigger_time", "trigger_dt", "disable_btn"])

    @property
    def icon(self):
        """return icon."""
        return 'mdi:light-switch'
    
    @property
    def disable_btn(self):
        """Return the button physical control."""
        return self._attr_disable_btn == 1

    async def async_update(self):
        resp = await self.async_fetch_res_values()
        if resp:
            for x in resp:
                await self.async_set_attr(x["resourceId"], x["value"], x["timeStamp"], write_ha_state=False)
                if x["resourceId"] in DISABLE_MAPPING.keys():
                    dbtns = await self.async_fetch_res_values(DISABLE_MAPPING.get(x["resourceId"]))
                    if dbtns:
                        self._attr_disable_btn = int(dbtns[0]["value"])

    def convert_res_to_attr(self, res_name, res_value):
        if res_name == "toggle" or res_name == "decoupled":
            return res_value == "1"
        if res_name == "energy":
            return round(float(res_value) / 1000.0, 3)
        if res_name == "firmware_version":
            return res_value
        if res_name == "zigbee_lqi":
            return int(res_value)
        return super().convert_res_to_attr(res_name, res_value)
