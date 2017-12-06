"""
The "user settings platform" platform.

"""

import logging
from custom_components.user_settings import UserSettingsComponent

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    _LOGGER.info("Setting up UserSettingsPlatform.")

    add_devices([UserSettingsPlatform()])


class UserSettingsPlatform(UserSettingsComponent):
    """Representation of user setting."""

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
        return 'Device Settings'

