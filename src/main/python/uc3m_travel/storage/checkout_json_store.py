"""This module handles JSON storage for hotel checkout management in the uc3m_travel system"""
from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException


class CheckoutJsonStore(JsonStore):
    """Provides singleton access to the JSON store for checkout data"""

    # pylint: disable=invalid-name
    class __CheckoutJsonStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_check_out.json"

        def add_item(self, item):
            # check if reservation already exists
            checkout_found = self.find_item("room_key", item["room_key"])
            if checkout_found:
                raise HotelManagementException("Guest is already out")

            super().load_list_from_file()
            self._data_list.append(item)
            super().save_list_to_file()

    __instance = None

    def __new__(cls):
        if not CheckoutJsonStore.__instance:
            CheckoutJsonStore.__instance = CheckoutJsonStore.__CheckoutJsonStore()
        return CheckoutJsonStore.__instance
