"""Id card attribute"""
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.attributes.attribute import Attribute

# pylint: disable=too-few-public-methods
class IdCard(Attribute):
    """Definition of attribute Id Number"""
    def __init__(self, id_card):
        # pylint: disable=arguments-renamed
        super().__init__()
        self._validation_pattern = r"^[0-9]{8}[A-Z]{1}$"
        self._error_message = "Invalid IdCard format"
        self._attr_value = self._validate(id_card)

    # pylint: disable=arguments-renamed
    def _validate(self, id_card):
        # pylint: disable=arguments-renamed
        super()._validate(id_card)

        def validate_dni(d):
            """RETURN TRUE IF THE DNI IS RIGHT, OR FALSE IN OTHER CASE"""
            c = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
                 "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
                 "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
                 "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}
            v = int(d[0:8])
            r = str(v % 23)
            return d[8] == c[r]

        if not validate_dni(id_card):
            raise HotelManagementException("Invalid IdCard letter")
        return id_card

        # valid_characters = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
        #      "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
        #      "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
        #      "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}
        # id_number = int(id_card[0:8])
        # id_module = str(id_number % 23)
        # if id_card[8] != valid_characters[id_module]:
        #     raise HotelManagementException("Invalid IdCard letter")
