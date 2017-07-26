"""
The "transactive home" component.

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

DOMAIN = "transactive_home"
FROM = "from"
SCAN_INTERVAL = timedelta(3600)

DEPENDENCIES = []

def setup(hass, config):
    """Setup our skeleton component."""

    _LOGGER.info("Transacive Home loading.")
    
    component = EntityComponent(_LOGGER, DOMAIN, hass, SCAN_INTERVAL)

    component.setup(config)

    descriptions = load_yaml_config_file(
        os.path.join(os.path.dirname(__file__), 'services.yaml'))

    def update_transactive_home(service):
        """Do any update to the component."""
        # _LOGGER.info("transactive home service object: %s", service)
        # _LOGGER.info("what is in here?: %s", hass)
        
        update_obj = service.data.get('value')

        # _LOGGER.info("state attributes: %s", hass.states.get('transactive_home.transactive_home'))

        transactive_home = hass.states.get('transactive_home.transactive_home').as_dict()
        attributes = transactive_home["attributes"]

        # _LOGGER.info("writing value: %s", update_obj)

        attributes["overallflexibility"][0][update_obj["target"]] = update_obj["value"]

        hass.states.set('transactive_home.transactive_home', State.from_dict(transactive_home), attributes, True)

        _LOGGER.info("transactive home after update: %s", hass.states.get('transactive_home.transactive_home'))


        # transactive_homes = component.extract_from_service(service)

        # for transactive_home in transactive_homes:
        #     transactive_home.set_transactive_home(kwargs)

        # hass.services.call(DOMAIN, 'update_transactive_home', kwargs)

    hass.services.register(
        DOMAIN,
        'update_transactive_home',
        update_transactive_home,
        descriptions['update_transactive_home'])

    def update_transactive_home_device(service):
        """Update a transactive home device."""
        
        update_obj = service.data.get('value')

        transactive_home = hass.states.get('transactive_home.transactive_home').as_dict()
        
        attributes = transactive_home["attributes"]

        _LOGGER.info("damn devices: %s", attributes["device"])

        _LOGGER.info("update value: %s", update_obj["value"])
        
        for dev in attributes["device"]:
            if (dev["name"] == update_obj["device"]):
                dev[update_obj["target"]] = update_obj["value"]

        transactive_home["attributes"] = attributes

        hass.states.set('transactive_home.transactive_home', 'On', attributes, True)

        _LOGGER.info("device after update: %s", hass.states.get('transactive_home.transactive_home'))

    hass.services.register(
        DOMAIN,
        'update_transactive_home_device',
        update_transactive_home_device,
        descriptions['update_transactive_home_device'])

    return True


class TransactiveComponent(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""

        _LOGGER.info("TransactivePlatform loading.")

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Transactive Home'

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
            "overallflexibility":[{
                    "flexibility": 10,
                    "zone_min": 0,
                    "zone_max": 100
                }],
            "measures": [{
                    "label": "Overall Reduction",
                    "value": 51,
                    "unit": "kw"
                },
                {
                    "label": "Overall Energy",
                    "value": 80,
                    "unit": "kw-hr/24 hrs"
                },
                {
                    "label": "Overall Power",
                    "value": 12,
                    "unit": "kw"
                }
            ],
            "chartSeries": [
                {
                    "data": [
                        ['2017-07-17 23:36:58.368599Z', 4],
                        ['2017-07-17 23:37:08.368599Z', 5],
                        ['2017-07-17 23:37:18.368599Z', 7],
                    ],
                    "type": "line",
                    "label": "energy"
                },
                {
                    "data": [
                        ['2017-08-17 23:36:58.368599Z', 8, 9,10],
                        ['2017-08-17 23:37:08.368599Z', 7, 7,9],
                        ['2017-08-17 23:37:18.368599Z', 6, 5,8],
                    ],
                    "type": "bar",
                    "label": "power"
                }
            ],
            "device": [{
                    "name": "device1",
                    "participate": "true",
                    "zone_min": 0,
                    "zone_max": 1,
                    "power": 150,
                    "energy": 40
                },
                {
                    "name": "device2",
                    "participate": "true",
                    "zone_min": 0,
                    "zone_max": 1,
                    "power": 15,
                    "energy": 30
                }
            ]
        }

        return data
