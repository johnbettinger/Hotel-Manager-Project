"""Arrival date attribute"""
from uc3m_travel.attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class ArrivalDate(Attribute):
    """Definition of attribute Arrival Date"""
    def __init__(self, arrival_date):
        super().__init__()
        self._validation_pattern = r"^(([0-2]\d|-3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$"
        self._error_message = "Invalid date format"
        self._attr_value = self._validate(arrival_date)
