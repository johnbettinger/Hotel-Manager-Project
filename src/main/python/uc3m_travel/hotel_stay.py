''' Class HotelStay (GE2.2) '''
from datetime import datetime
import hashlib

from uc3m_travel import HotelReservation
from uc3m_travel.attributes.attribute_room_key import RoomKey
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.storage.checkout_json_store import CheckoutJsonStore
from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.storage.stay_json_store import StayJsonStore


class HotelStay():
    """Class for representing hotel stays"""
    def __init__(self,
                 idcard:str,
                 localizer:str,
                 numdays:int,
                 roomtype:str):
        """constructor for HotelStay objects"""
        self.__alg = "SHA-256"
        self.__type = roomtype
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = datetime.timestamp(justnow)
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express num_days in seconds
        self.__departure = self.__arrival + (numdays * 24 * 60 * 60)
        self.__room_key = hashlib.sha256(self.__signature_string().encode()).hexdigest()
    @classmethod
    def create_guest_arrival_from_file(cls, file_input):
        """Helper to create an arrival from a file"""
        json_helper = JsonStore()
        input_list = JsonStore.read_input_file(json_helper, file_input)
        # comprobar valores del fichero
        my_id_card, my_localizer = JsonStore.read_input_data_from_file(json_helper, input_list)
        new_reservation = HotelReservation.create_reservation_from_arrival(my_id_card, my_localizer)
        # compruebo si hoy es la fecha de checkin
        reservation_format = "%d/%m/%Y"
        date_obj = datetime.strptime(new_reservation.arrival, reservation_format)
        if date_obj.date() != datetime.date(datetime.utcnow()):
            raise HotelManagementException("Error: today is not reservation date")
        # genero la room key para ello llamo a Hotel Stay
        my_checkin = HotelStay(idcard=my_id_card, numdays=int(new_reservation.num_days),
                               localizer=my_localizer, roomtype=new_reservation.room_type)
        return my_checkin

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
            ",departure:" + str(self.__departure) + "}"

    @property
    def id_card(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return self.__room_key

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        """returns the value of the departure date"""
        self.__departure = value


    # def validate_localizer(self, localizer):
    #     """validates the localizer format using a regex"""
    #     r = r'^[a-fA-F0-9]{32}$'
    #     myregex = re.compile(r)
    #     if not myregex.fullmatch(localizer):
    #         raise HotelManagementException("Invalid localizer")
    #     return localizer
    #
    # def validate_roomkey(self, roomkey):
    #     """validates the roomkey format using a regex"""
    #     r = r'^[a-fA-F0-9]{64}$'
    #     myregex = re.compile(r)
    #     if not myregex.fullmatch(roomkey):
    #         raise HotelManagementException("Invalid room key format")
    #     return roomkey

    # pylint: disable=unused-private-member
    @classmethod
    def get_hotel_stay_from_room_key(cls, room_key):
        """Helper to create a hotel stay from the room key """
        my_room_key = RoomKey(room_key).value
       # HotelStay.validate_roomkey(cls, room_key)

        file_checkin_store = StayJsonStore()
        new_stay = file_checkin_store.find_item(key="_HotelStay__room_key",
                                                value=my_room_key)
        # if we were able to identify a room key ....
        if new_stay:
            my_stay = HotelStay(idcard=new_stay["_HotelStay__idcard"],
                                numdays=0, localizer=new_stay["_HotelStay__localizer"],
                                roomtype=new_stay["_HotelStay__type"])
            my_stay.__room_key = my_room_key
            my_stay.__departure = new_stay["_HotelStay__departure"]
            return my_stay
        raise HotelManagementException("Error: room key not found")

    def check_out(self):
        """Check out function"""
        today = datetime.utcnow().date()
        if datetime.fromtimestamp(self.departure).date() != today:
            raise HotelManagementException("Error: today is not the departure day")
        file_store_checkout = CheckoutJsonStore()
        if file_store_checkout.find_item(key="room_key",
                                         value=self.room_key):
            raise HotelManagementException("Guest is already out")
        room_checkout = {"room_key": self.room_key, "checkout_time":
            datetime.timestamp(datetime.utcnow())}
        file_store_checkout.add_item(room_checkout)
