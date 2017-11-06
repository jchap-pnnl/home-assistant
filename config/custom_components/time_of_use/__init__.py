"""
The "time of use" component.

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

DOMAIN = "time_of_use"
FROM = "from"
SCAN_INTERVAL = timedelta(3600)

DEPENDENCIES = []

def setup(hass, config):
    """Setup our skeleton component."""

    _LOGGER.info("Time of Use loading.")
    
    component = EntityComponent(_LOGGER, DOMAIN, hass, SCAN_INTERVAL)

    component.setup(config)

    descriptions = load_yaml_config_file(
        os.path.join(os.path.dirname(__file__), 'services.yaml'))

    def update_time_of_use(service):
        """Do any update to the component."""
        # _LOGGER.info("time of use service object: %s", service)
        # _LOGGER.info("what is in here?: %s", hass)
        
        update_obj = service.data.get('value')

        # _LOGGER.info("state attributes: %s", hass.states.get('time_of_use.time_of_use'))

        time_of_use = hass.states.get('time_of_use.time_of_use').as_dict()
        attributes = time_of_use["attributes"]

        # _LOGGER.info("writing value: %s", update_obj)

        attributes["overallflexibility"][0][update_obj["target"]] = update_obj["value"]

        hass.states.set('time_of_use.time_of_use', State.from_dict(time_of_use), attributes, True)

        _LOGGER.info("Time of Use after update: %s", hass.states.get('time_of_use.time_of_use'))

    hass.services.register(
        DOMAIN,
        'update_time_of_use',
        update_time_of_use,
        descriptions['update_time_of_use'])

    return True


class TimeOfUseComponent(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""

        _LOGGER.info("TimeOfUsePlatform loading.")

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Time of Use'

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
                "maximum": "11",
                "minimum": "0",
                "transactive": "5"
            },
            "energyCost":{
                "maximum": "$50.00",
                "minimum": "$0",
                "transactive": "$8.75"
            }
        }

        return data
