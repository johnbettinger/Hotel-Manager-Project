"""Credit card attribute"""
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class CreditCard(Attribute):
    """Definition of attribute Credit Card Number"""
    def __init__(self, credit_card):
        super().__init__()
        self._validation_pattern = r"^[0-9]{16}"
        self._error_message = "Invalid credit card format"
        self._attr_value = self._validate(credit_card)

    # pylint: disable=arguments-renamed
    def _validate(self, credit_card):
        # pylint: disable=arguments-renamed
        super()._validate(credit_card)
        def digits_of(n):
            return [int(d) for d in str(n)]


        digits = digits_of(credit_card)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        if not checksum % 10 == 0:
            raise HotelManagementException("Invalid credit card number (not luhn)")
        return credit_card
