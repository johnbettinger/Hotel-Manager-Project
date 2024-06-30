"""Module for the hotel manager"""
import os
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.storage.reservation_json_store import ReservationJsonStore
from uc3m_travel.storage.stay_json_store import StayJsonStore
#from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_stay import HotelStay


# pylint: disable=too-few-public-methods
class HotelManager:
    """Hotel Manager Class"""

    # pylint: disable=invalid-name
    class __HotelManager:
        """Class with all the methods for managing reservations and stays"""

        def __init__(self):
            pass

        # pylint: disable=too-many-arguments
        def room_reservation(self,
                             credit_card: str,
                             name_surname: str,
                             id_card: str,
                             phone_number: str,
                             room_type: str,
                             arrival_date: str,
                             num_days: int) -> str:
            """manges the hotel reservation: creates a reservation and saves it into a json file"""

            my_reservation = HotelReservation(id_card=id_card,
                                              credit_card_number=credit_card,
                                              name_surname=name_surname,
                                              phone_number=phone_number,
                                              room_type=room_type,
                                              arrival=arrival_date,
                                              num_days=num_days)

            reservation_store = ReservationJsonStore()
            reservation_store.save_reservation(my_reservation)

            return my_reservation.localizer

        def guest_arrival(self, file_input: str) -> str:
            """manages the arrival of a guest with a reservation"""

            my_checkin = HotelStay.create_guest_arrival_from_file(file_input)

            stay_store = StayJsonStore()
            stay_store.save_checkin(my_checkin)

            return my_checkin.room_key

        def guest_checkout(self, room_key: str) -> bool:
            """checks out a hotel stay"""
            file_store_check_in = JSON_FILES_PATH + "store_check_in.json"
            if not os.path.isfile(file_store_check_in):
                raise HotelManagementException("Error: file input not found")
            stay_to_checkout = HotelStay.get_hotel_stay_from_room_key(room_key)
            stay_to_checkout.check_out()
            return True

    __instance = None

    def __new__(cls):
        if not HotelManager.__instance:
            HotelManager.__instance = HotelManager.__HotelManager()
        return HotelManager.__instance
