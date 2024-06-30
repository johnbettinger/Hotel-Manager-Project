"""Room type attribute"""
from uc3m_travel.attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class RoomType(Attribute):
    """Definition of attribute Name and Surname"""
    def __init__(self, room_type):
        super().__init__()
        self._validation_pattern = r"(SINGLE|DOUBLE|SUITE)"
        self._error_message = "Invalid roomtype value"
        self._attr_value = self._validate(room_type)
