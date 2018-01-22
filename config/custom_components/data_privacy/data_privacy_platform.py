"""
The "data privacy platform" platform.

"""

import logging
from custom_components.data_privacy import DataPrivacyComponent

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    _LOGGER.info("Setting up DataPrivacyPlatform.")

    add_devices([DataPrivacyPlatform()])


class DataPrivacyPlatform(DataPrivacyComponent):
    """Representation of the data privacy platform."""

    def __init__(self):
        """Initialize the platform."""
        self._state = 'connected_homes'

    @property
    def state(self):
        """Return the state of the platform."""
        return self._state

    @property
    def name(self):
        """Return the name of the platform."""
        return 'Data Privacy'

