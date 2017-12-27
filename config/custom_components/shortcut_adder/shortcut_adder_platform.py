"""
The "shortcut adder platform" platform.

"""

import logging
from custom_components.shortcut_adder import ShortcutAdderComponent

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    _LOGGER.info("Setting up ShortcutAdderPlatform.")

    add_devices([ShortcutAdderPlatform()])


class ShortcutAdderPlatform(ShortcutAdderComponent):
    """Representation of shortcut adder."""

    def __init__(self):
        """Initialize the shortcut adder."""
        self._state = 'On'

    @property
    def state(self):
        """Return the state of the shortcut adder."""
        return self._state

    @property
    def name(self):
        """Return the name of the shortcut adder."""
        return 'shortcut adder'

