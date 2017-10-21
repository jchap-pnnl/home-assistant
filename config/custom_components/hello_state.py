"""
The "hello world" custom component.

This component implements the bare minimum that a component should implement.

Configuration:

To use the hello_word component you will need to add the following to your
configuration.yaml file.

hello_world:
"""

import logging

_LOGGER = logging.getLogger(__name__)

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "hello_state"

# List of component names (string) your component depends upon.
DEPENDENCIES = []


def setup(hass, config):
    """Setup our skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('goodbye.failing', 'JoeyChaps!')
    hass.states.set('hello.success', config[DOMAIN]['from'])

    _LOGGER.info("Consider yourself logged!")
    # Return boolean to indicate that initialization was successfully.
    return True
