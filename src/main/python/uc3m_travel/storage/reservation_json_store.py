"""Module for managing JSON storage specific to hotel reservations"""
from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException

class ReservationJsonStore(JsonStore):
    """Provides a singleton access point to manage reservation data in a JSON store"""

    # pylint: disable=invalid-name
    class __ReservationJsonStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_reservation.json"

        # CREATE FIND ITEM METHOD?

        def add_item(self, item):
            # check if reservation already exists
            reservation_found = self.find_item("_HotelReservation__localizer",
                item.localizer)
            if reservation_found:
                raise HotelManagementException(
                    "Reservation already exists")

            # check if reservation already exists under id
            id_card_found = self.find_item("_HotelReservation__id_card", item.id_card)
            if id_card_found:
                raise HotelManagementException("This ID card has another reservation")

            super().add_item(item)

    __instance = None

    def __new__(cls):
        if not ReservationJsonStore.__instance:
            ReservationJsonStore.__instance = ReservationJsonStore.__ReservationJsonStore()
        return ReservationJsonStore.__instance
