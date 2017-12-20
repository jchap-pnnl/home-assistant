"""
The "extras platform" platform.

"""

import logging
from custom_components.extras import ExtrasComponent

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    _LOGGER.info("Setting up ExtrasPlatform.")

    add_devices([ExtrasPlatform()])


class ExtrasPlatform(ExtrasComponent):
    """Representation of extras."""

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
        return 'Extras'

