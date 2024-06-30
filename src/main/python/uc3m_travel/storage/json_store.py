"""This module provides JSON storage management for hotel management operations"""
import json
import hashlib
from uc3m_travel.hotel_management_exception import HotelManagementException


class JsonStore():
    """Manages JSON data storage for hotel management operations"""
    _data_list = []
    _file_name = ""

    def __init__(self):
        """Initialize the JsonStore by loading data from a file"""
        self.load_list_from_file()

    def save_reservation(self, reservation_data):
        """Save reservation data to the JSON file"""
        # Directly use add_item to handle load and save logic
        self.add_item(reservation_data)

    def save_checkin(self, checkin_data):
        """Save check-in data to the JSON file"""
        # Directly use add_item to handle load and save logic
        self.add_item(checkin_data)

    def save_checkout(self, checkout_data):
        """Save check-out data to the JSON file"""
        # Directly use add_item to handle load and save logic
        self.add_item(checkout_data)

    def save_list_to_file(self):
        """Save the data list to a JSON file."""
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise HotelManagementException("Wrong file or file path") from ex

    def load_and_create(self):
        """Load data list from file or create a new list if the file does not exist"""
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

    def load_list_from_file(self):
        """Load data list from the JSON file"""
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex

    def add_item(self, item):
        """Add a new item to the JSON store and save the updated list"""
        self.load_list_from_file()
        self._data_list.append(item.__dict__)
        self.save_list_to_file()

    def find_item(self, key, value):
        """Find an item by key and value"""
        self.load_list_from_file()
        for item in self._data_list:
            if item[key] == value:
                return item
        return None

    @property
    def hash(self):
        """Compute a hash of the stored data for integrity verification"""
        self.load_list_from_file()
        return hashlib.md5(str(self).encode()).hexdigest()

    def read_input_file(self, file_input):
        """Read data from a specified input file"""
        try:
            with open(file_input, "r", encoding="utf-8", newline="") as file:
                input_list = json.load(file)
        except FileNotFoundError as ex:
            raise HotelManagementException("Error: file input not found") from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return input_list

    def read_input_data_from_file(self, input_list):
        """Parse specific data from a given list, returning id_card and localizer"""
        try:
            my_localizer = input_list["Localizer"]
            my_id_card = input_list["IdCard"]
        except KeyError as e:
            raise HotelManagementException("Error - Invalid Key in JSON") from e
        return my_id_card, my_localizer
