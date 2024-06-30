"""Hotel reservation class"""
import hashlib
from datetime import datetime, timezone

from uc3m_travel.attributes.attribute_cc_number import CreditCard
from uc3m_travel.attributes.attribute_id_number import IdCard
from uc3m_travel.attributes.attribute_num_days import NumDays
from uc3m_travel.attributes.attribute_phone_number import PhoneNumber
from uc3m_travel.attributes.attribute_name_surname import NameSurname
from uc3m_travel.attributes.attribute_room_type import RoomType
from uc3m_travel.attributes.attribute_arrival_date import ArrivalDate
from uc3m_travel.attributes.attribute_localizer import Localizer
from uc3m_travel.storage.reservation_json_store import ReservationJsonStore
from uc3m_travel.hotel_management_exception import HotelManagementException
from freezegun import freeze_time


class HotelReservation:
    # pylint: disable=too-many-arguments, too-many-instance-attributes
    """Manage Hotel Reservation Class"""

    @classmethod
    def create_reservation_from_arrival(cls, my_id_card, my_localizer):
        """creating reservation class method"""
        my_id_card = IdCard(my_id_card).value
        my_localizer = Localizer(my_localizer).value
        reservations_store = ReservationJsonStore()
        reservation = reservations_store.find_item(key="_HotelReservation__localizer",
                                                   value=my_localizer)
        # buscar en almacen
        # compruebo si esa reserva esta en el almacen
        if reservation is None:
            raise HotelManagementException("Error: localizer not found")
        if my_id_card != reservation["_HotelReservation__id_card"]:
            raise HotelManagementException("Error: Localizer is not correct for this IdCard")
        # regenrar clave y ver si coincide
        reservation_date = (
            datetime.fromtimestamp(reservation["_HotelReservation__reservation_date"]))
        with freeze_time(reservation_date):
            new_reservation = HotelReservation(credit_card_number=
                                        reservation["_HotelReservation__credit_card_number"],
                                        id_card=reservation["_HotelReservation__id_card"],
                                        num_days=reservation["_HotelReservation__num_days"],
                                        room_type=reservation["_HotelReservation__room_type"],
                                        arrival=reservation["_HotelReservation__arrival"],
                                        name_surname=reservation["_HotelReservation__name_surname"],
                                        phone_number=reservation["_HotelReservation__phone_number"])
        if new_reservation.localizer != my_localizer:
            raise HotelManagementException("Error: reservation has been manipulated")
        return new_reservation

    def __init__(self,
                 id_card: str,
                 credit_card_number: str,
                 name_surname: str,
                 phone_number: str,
                 room_type: str,
                 arrival: str,
                 num_days: int):
        """constructor of reservation objects"""
        self.__credit_card_number = CreditCard(credit_card_number).value
        self.__id_card = IdCard(id_card).value
        justnow = datetime.now(timezone.utc)
        self.__arrival = ArrivalDate(arrival).value
        self.__reservation_date = datetime.timestamp(justnow)
        self.__name_surname = NameSurname(name_surname).value
        self.__phone_number = PhoneNumber(phone_number).value
        self.__room_type = RoomType(room_type).value
        self.__num_days = NumDays(num_days).value
        self.__localizer = hashlib.md5(str(self).encode()).hexdigest()

    # def validate_credit_card( self, x ):
    #     """validates the credit card number using luhn altorithm"""
    #     #taken form
    #     # https://allwin-raju-12.medium.com/
    #     # credit-card-number-validation-using-luhns-algorithm-in-python-c0ed2fac6234
    #     # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
    #     # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
    #
    #     myregex = re.compile(r"^[0-9]{16}")
    #     res = myregex.fullmatch(x)
    #     if not res:
    #         raise HotelManagementException("Invalid credit card format")
    #     def digits_of(n):
    #         return [int(d) for d in str(n)]
    #
    #
    #     digits = digits_of(x)
    #     odd_digits = digits[-1::-2]
    #     even_digits = digits[-2::-2]
    #     checksum = 0
    #     checksum += sum(odd_digits)
    #     for d in even_digits:
    #         checksum += sum(digits_of(d * 2))
    #     if not checksum % 10 == 0:
    #         raise HotelManagementException("Invalid credit card number (not luhn)")
    #     return x
    #
    # def validate_room_type(self, room_type):
    #     """validates the room type value using regex"""
    #     myregex = re.compile(r"(SINGLE|DOUBLE|SUITE)")
    #     res = myregex.fullmatch(room_type)
    #     if not res:
    #         raise HotelManagementException("Invalid roomtype value")
    #     return room_type

    # def validate_arrival_date(self, arrival_date):
    #     """validates the arrival date format  using regex"""
    #     myregex = re.compile(r"^(([0-2]\d|-3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$")
    #     res = myregex.fullmatch(arrival_date)
    #     if not res:
    #         raise HotelManagementException("Invalid date format")
    #     return arrival_date

    # def validate_num_days(self,num_days):
    #     """validates the number of days"""
    #     try:
    #         days = int(num_days)
    #     except ValueError as ex:
    #         raise HotelManagementException("Invalid num_days datatype") from ex
    #     if (days < 1 or days > 10):
    #         raise HotelManagementException("Numdays should be in the range 1-10")
    #     return num_days

    # def validate_phone_number(self, phone_number):
    #     """validates the phone number format  using regex"""
    #     myregex = re.compile(r"^(\+)[0-9]{9}")
    #     res = myregex.fullmatch(phone_number)
    #     if not res:
    #         raise HotelManagementException("Invalid phone number format")
    #     return phone_number

    # def validate_name_surname(self, name):
    #     r = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
    #     myregex = re.compile(r)
    #     regex_matches = myregex.fullmatch(name)
    #     if not regex_matches:
    #         raise HotelManagementException("Invalid name format")
    #     return name
    #
    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        # VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__id_card,
                     "name_surname": self.__name_surname,
                     "credit_card": self.__credit_card_number,
                     "phone_number:": self.__phone_number,
                     "reservation_date": self.__reservation_date,
                     "arrival_date": self.__arrival,
                     "num_days": self.__num_days,
                     "room_type": self.__room_type,
                     }
        return "HotelReservation:" + json_info.__str__()

    @property
    def credit_card(self):
        """property for getting and setting the credit_card number"""
        return self.__credit_card_number

    @credit_card.setter
    def credit_card(self, value):
        self.__credit_card_number = value

    @property
    def id_card(self):
        """property for getting and setting the id_card"""
        return self.__id_card

    @id_card.setter
    def id_card(self, value):
        self.__id_card = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        return self.__localizer

    @property
    def arrival(self):
        """Returns the md5 signature"""
        return self.__arrival

    @property
    def num_days(self):
        """Returns the md5 signature"""
        return self.__num_days

    @property
    def room_type(self):
        """Returns the md5 signature"""
        return self.__room_type
