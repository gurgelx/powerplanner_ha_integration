"""Contains the base entity."""

import hashlib

from homeassistant.helpers.entity import Entity

from .const import DOMAIN


class PowerPlannerEntityBase(Entity):
    """Base entity for powerplanner."""

    def __init__(self, apiKey: str) -> None:
        """Init the class with the device id."""
        self.device_id = self.__stable_hash_id(apiKey)

    @property
    def device_info(self):
        """Return the device info."""
        info = {
            "identifiers": {(DOMAIN, self.device_id)},
            "name": "PowerPlanner",
            "manufacturer": "NomKon AB",
            "configuration_url": "https://www.powerplanner.se",
        }
        return info

    def __stable_hash_id(self, s: str) -> int:
        """Return a stable hash id."""
        return int(hashlib.md5(s.encode()).hexdigest(), 16)
