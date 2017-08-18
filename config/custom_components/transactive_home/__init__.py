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
        _LOGGER.info(service)
        _LOGGER.info("------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        update_obj = service.data.get('value')
        _LOGGER.info(update_obj)
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
            "progress_bar": {
                "message": "Half-way through, keep up the good work!",
                "value": 55,
                "starting_point": 0,
                "end_point": 80
            },
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
                    "times": [
                        '2017-07-17 23:36:58.368599Z',
                        '2017-07-17 23:37:28.368599Z',
                        '2017-07-17 23:37:58.368599Z',
                        '2017-07-17 23:38:28.368599Z',
                        '2017-07-17 23:38:58.368599Z',
                        '2017-07-17 23:39:28.368599Z',
                        '2017-07-17 23:39:58.368599Z',
                        '2017-07-17 23:40:28.368599Z',
                        '2017-07-17 23:40:58.368599Z',
                        '2017-07-17 23:41:28.368599Z'
                    ],
                    "historical": [ 3, 4, 6, 6, 7, 9, 11, 13, 16, 17 ],
                    "actual": [ 4, 5, 7, 8, None, None, None, None, None, None ],
                    "transactive": [ 4, 5, 7, 8, 8, 8, 9, 9, 10, 12 ],
                    "type": "line",
                    "label": "energy"
                }
            ]
        }

        return data
