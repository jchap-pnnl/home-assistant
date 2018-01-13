"""
The "whole house energy platform" platform.

"""

import logging
from custom_components.whole_house_energy import WholeHouseEnergyComponent

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""

    _LOGGER.info("Setting up WholeHouseEnergyPlatform.")

    add_devices([WholeHouseEnergyPlatform()])


class WholeHouseEnergyPlatform(WholeHouseEnergyComponent):
    """Representation of a demo climate device."""

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
        return 'Whole-house energy use and cost'

    def set_whole_house_energy(self: WholeHouseEnergyComponent, new_value):
        _LOGGER.info("In component set_whole_house_energy method")
        # _LOGGER.info("slider value: %s", new_value)
        # self._state = {'slider_value': new_value.slider_value}
        # _LOGGER.info("state: %s", self._state)
        # self.state_attributes["device"][0]["flexibility"] = new_value
        # _LOGGER.info("whole house enerrgy component device flexibility: %s", self.state_attributes["device"][0]["flexibility"])

