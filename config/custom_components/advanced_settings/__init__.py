"""
The "advanced settings" component.

"""

import asyncio
import logging
import os
import json
from datetime import timedelta
from homeassistant.config import load_yaml_config_file
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.core import State


_LOGGER = logging.getLogger(__name__)

DOMAIN = "advanced_settings"
FROM = "from"
SCAN_INTERVAL = timedelta(3600)

DEPENDENCIES = []

def setup(hass, config):
    """Setup our skeleton component."""

    _LOGGER.info("Advanced Settings loading.")
    
    component = EntityComponent(_LOGGER, DOMAIN, hass, SCAN_INTERVAL)

    component.setup(config)

    descriptions = load_yaml_config_file(
        os.path.join(os.path.dirname(__file__), 'services.yaml'))

    def update_advanced_settings(service):
        """Do any update to the component."""
        
        update_obj = service.data.get('value')

        _LOGGER.info("update object: %s", update_obj)

        advanced_settings = hass.states.get('advanced_settings.advanced_settings').as_dict()
        attributes = advanced_settings["attributes"]

        if update_obj["subtarget"] is not None:
            attributes[update_obj["target"]][update_obj["subtarget"]] = update_obj["value"]
        else:
            attributes[update_obj["target"]] = update_obj["value"]

        hass.states.set('advanced_settings.advanced_settings', State.from_dict(advanced_settings), attributes, True)

        _LOGGER.info("advanced settings after update: %s", hass.states.get('advanced_settings.advanced_settings'))

    hass.services.register(
        DOMAIN,
        'update_advanced_settings',
        update_advanced_settings,
        descriptions['update_advanced_settings'])

    return True


class AdvancedSettingsComponent(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""

        _LOGGER.info("AdvancedSettingsPlatform loading.")

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Advanced Settings'

    @property
    def state(self):
        """Card state."""
        return 'happy'

    @property
    def state_attributes(self):
        """Return the optional state attributes."""

        data = {
            "energySavings":{
                "goal": "2",
                "unit": "Kw"
            },
            "savingsStartTime": "10:00am",
            "savingsEndTime": "5:00pm"
        }

        return data
