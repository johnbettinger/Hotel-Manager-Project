"""Num days attribute"""
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class NumDays(Attribute):
    """Definition of attribute Num Days"""
    def __init__(self, num_days):
        # pylint: disable=arguments-renamed
        super().__init__()
        self._validation_pattern = r""
        self._error_message = ""
        self._attr_value = self._validate(num_days)

    # pylint: disable=arguments-renamed
    def _validate(self, num_days):
        # pylint: disable=arguments-renamed
        try:
            days = int(num_days)
        except ValueError as ex:
            raise HotelManagementException("Invalid num_days datatype") from ex
        if (days < 1 or days > 10):
            raise HotelManagementException("Numdays should be in the range 1-10")
        return num_days
