"""Room key attribute"""
from uc3m_travel.attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class RoomKey(Attribute):
    """Definition of attribute Room Key"""
    def __init__(self, room_key):
        super().__init__()
        self._validation_pattern = r'^[a-fA-F0-9]{64}$'
        self._error_message = "Invalid room key format"
        self._attr_value = self._validate(room_key)
