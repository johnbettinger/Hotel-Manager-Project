"""Name attribute"""
from uc3m_travel.attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class NameSurname(Attribute):
    """Definition of attribute Name and Surname"""
    def __init__(self, name_surname):
        super().__init__()
        self._validation_pattern = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
        self._error_message = "Invalid name format"
        self._attr_value = self._validate(name_surname)
