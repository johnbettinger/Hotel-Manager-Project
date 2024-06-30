"""Phone attribute"""
from uc3m_travel.attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class PhoneNumber(Attribute):
    """Definition of attribute Phone Number"""
    def __init__(self, phone_number):
        super().__init__()
        self._validation_pattern = r"^(\+)[0-9]{9}"
        self._error_message = "Invalid phone number format"
        self._attr_value = self._validate(phone_number)


    # def _validate(self, attr_value):
    #     super()._validate(attr_value)
