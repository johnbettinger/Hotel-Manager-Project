"""Module for managing JSON storage specific to hotel stay records, particularly check-ins"""
from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException

class StayJsonStore(JsonStore):
    """Manages a singleton instance for JSON storage of hotel stay data"""
    # pylint: disable=invalid-name
    class __StayJsonStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_check_in.json"

        def add_item(self, item):
            # check if room key already exists
            room_key_found = self.find_item("_HotelStay__room_key", item.room_key)
            if room_key_found:
                raise HotelManagementException("ckeckin  ya realizado")

            super().add_item(item)

    __instance = None

    def __new__(cls):
        if not StayJsonStore.__instance:
            StayJsonStore.__instance = StayJsonStore.__StayJsonStore()
        return StayJsonStore.__instance
