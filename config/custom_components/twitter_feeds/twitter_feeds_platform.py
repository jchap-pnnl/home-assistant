"""
The "twitter feeds platform" platform.

"""

import logging
from custom_components.twitter_feeds import TwitterFeedsComponent

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    _LOGGER.info("Setting up TwitterFeedsPlatform.")

    add_devices([TwitterFeedsPlatform()])


class TwitterFeedsPlatform(TwitterFeedsComponent):
    """Representation of twitter feeds."""

    def __init__(self):
        """Initialize the climate device."""
        self._state = 'On'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Twitter Feeds'

