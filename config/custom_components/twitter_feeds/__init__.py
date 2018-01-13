"""
The "twitter feeds" component.

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

DOMAIN = "twitter_feeds"
FROM = "from"
SCAN_INTERVAL = timedelta(3600)

DEPENDENCIES = []

def setup(hass, config):
    """Setup our skeleton component."""

    _LOGGER.info("Twitter Feeds loading.")
    
    component = EntityComponent(_LOGGER, DOMAIN, hass, SCAN_INTERVAL)

    component.setup(config)

    descriptions = load_yaml_config_file(
        os.path.join(os.path.dirname(__file__), 'services.yaml'))

    def update_twitter_feeds(service):
        """Update the twitter feeds setting."""

        update_obj = service.data.get('value')

        _LOGGER.info("update_obj: %s", update_obj)

        update_value = update_obj["value"]

        twitter_feeds = hass.states.get('twitter_feeds.twitter_feeds').as_dict()

        attributes = twitter_feeds["attributes"]

        _LOGGER.info("before update: %s", attributes)
        _LOGGER.info("update value: %s", update_value)

        attributes["feeds_setting"] = update_value

        _LOGGER.info("after update: %s", attributes)

        hass.states.set('twitter_feeds.twitter_feeds', 'On', attributes, True)

    hass.services.register(
        DOMAIN,
        'update_twitter_feeds',
        update_twitter_feeds,
        descriptions['update_twitter_feeds'])

    return True


class TwitterFeedsComponent(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""

        _LOGGER.info("TwitterFeedsPlatform loading.")

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Twitter Feeds'

    @property
    def state(self):
        """Twitter feeds state."""
        return 'happy'

    @property
    def state_attributes(self):
        """Return the optional state attributes."""

        data = {
            "feeds_setting": "no_external",
            "feeds_options": [
                { 
                    "key": "no_external",
                    "label": "No external connections allowed. (most private)"
                },
                { 
                    "key": "vendor_updates",
                    "label": "Allow vendors to update your devices, but not share your data."
                },
                { 
                    "key": "allow_control",
                    "label": "Allow technicians and utilities to control devices for remote setup, diagnostics, and override. (least private)"
                }
            ]
        }

        return data
