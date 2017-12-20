"""
The "extras" component.

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

DOMAIN = "extras"
FROM = "from"
SCAN_INTERVAL = timedelta(3600)

DEPENDENCIES = []

def setup(hass, config):
    """Setup our skeleton component."""

    _LOGGER.info("Extras loading.")
    
    component = EntityComponent(_LOGGER, DOMAIN, hass, SCAN_INTERVAL)

    component.setup(config)

    descriptions = load_yaml_config_file(
        os.path.join(os.path.dirname(__file__), 'services.yaml'))

    def update_extras(service):
        """Update the extras setting."""

        update_obj = service.data.get('value')

        _LOGGER.info("update_obj: %s", update_obj)

        update_value = update_obj["value"]

        extras = hass.states.get('extras.extras').as_dict()

        attributes = extras["attributes"]

        _LOGGER.info("before update: %s", attributes)
        _LOGGER.info("update value: %s", update_value)

        attributes["privacy_setting"] = update_value

        _LOGGER.info("after update: %s", attributes)

        hass.states.set('extras.extras', 'On', attributes, True)

    hass.services.register(
        DOMAIN,
        'update_extras',
        update_extras,
        descriptions['update_extras'])

    return True


class ExtrasComponent(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""

        _LOGGER.info("ExtrasPlatform loading.")

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Extras'

    @property
    def state(self):
        """Extras state."""
        return 'happy'

    @property
    def state_attributes(self):
        """Return the optional state attributes."""

        data = {
            "extra_items": [
                { 
                    "key": "google",
                    "name": "Google",
                    "description": "Search the whole Internet",
                    "url": "www.google.com",
                    "button": "Search",
                    "image": "https://www.google.com/about/img/social/generic-feed.svg"
                },
                { 
                    "key": "twitter",
                    "name": "Twitter",
                    "description": "Post content to Twitter",
                    "url": "www.twitter.com",
                    "button": "Post",
                    "image": "http://redhint.com/wp-content/uploads/2017/09/Twitter.jpg"
                },
                { 
                    "key": "facebook",
                    "name": "Facebook",
                    "description": "Post content to Facebook",
                    "url": "www.facebook.com",
                    "button": "Post",
                    "image": "https://lh3.googleusercontent.com/ZZPdzvlpK9r_Df9C3M7j1rNRi7hhHRvPhlklJ3lfi5jk86Jd1s0Y5wcQ1QgbVaAP5Q=w170"
                },
                { 
                    "key": "utility",
                    "name": "City of Richland",
                    "description": "Pay your utility bill",
                    "url": "https://www.ci.richland.wa.us/departments/administrative-services/finance/utility-billing/pay-utility-bill-online",
                    "button": "Pay Bill",
                    "image": "https://pbs.twimg.com/profile_images/715323158379646980/G4qeTTkU.jpg"
                }
            ]
        }

        return data
