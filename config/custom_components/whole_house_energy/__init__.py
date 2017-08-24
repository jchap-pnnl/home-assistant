"""
The "whole house energy" component.

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

DOMAIN = "whole_house_energy"
FROM = "from"
SCAN_INTERVAL = timedelta(3600)

DEPENDENCIES = []

def setup(hass, config):
    """Setup our skeleton component."""

    _LOGGER.info("Whole House Energy loading.")
    
    component = EntityComponent(_LOGGER, DOMAIN, hass, SCAN_INTERVAL)

    component.setup(config)

    descriptions = load_yaml_config_file(
        os.path.join(os.path.dirname(__file__), 'services.yaml'))

    def update_whole_house_energy(service):
        """Do any update to the component."""
        # _LOGGER.info("whole house energy service object: %s", service)
        # _LOGGER.info("what is in here?: %s", hass)
        
        update_obj = service.data.get('value')

        # _LOGGER.info("state attributes: %s", hass.states.get('whole_house_energy.whole_house_energy'))

        whole_house_energy = hass.states.get('whole_house_energy.whole_house_energy').as_dict()
        attributes = whole_house_energy["attributes"]

        # _LOGGER.info("writing value: %s", update_obj)

        attributes["overallflexibility"][0][update_obj["target"]] = update_obj["value"]

        hass.states.set('whole_house_energy.whole_house_energy', State.from_dict(whole_house_energy), attributes, True)

        _LOGGER.info("whole house energy after update: %s", hass.states.get('whole_house_energy.whole_house_energy'))

    hass.services.register(
        DOMAIN,
        'update_whole_house_energy',
        update_whole_house_energy,
        descriptions['update_whole_house_energy'])

    return True


class WholeHouseEnergyComponent(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""

        _LOGGER.info("WholeHouseEnergyPlatform loading.")

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Whole House Energy'

    @property
    def state(self):
        """Camera state."""
        return 'happy'

    @property
    def overall_reduction(self):
        """Return the name of the sensor."""
        return 84

    @property
    def state_attributes(self):
        """Return the optional state attributes."""

        data = {
            "energyUse":{
                "maximum": "250",
                "minimum": "50",
                "transactive": "125"
            },
            "energyCost":{
                "maximum": "$37.50",
                "minimum": "$7.50",
                "transactive": "$18.75"
            }
        }

        return data
