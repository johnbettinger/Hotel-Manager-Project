"""Tests singletons"""
import unittest

from uc3m_travel import HotelManager
from uc3m_travel.storage.reservation_json_store import ReservationJsonStore
from uc3m_travel.storage.stay_json_store import StayJsonStore
from uc3m_travel.storage.checkout_json_store import CheckoutJsonStore
from uc3m_travel import HotelReservation


# pylint: disable=too-many-locals, duplicate-code
class MyTestCase(unittest.TestCase):
    """Test Case For The Singletons"""
    def test_singleton_hotel_manager(self):
        """Instance the three singletons and test they're equal
            Instance objects from non-singleton class and test they're different"""

        hotel_manager_1 = HotelManager()
        hotel_manager_2 = HotelManager()
        hotel_manager_3 = HotelManager()

        self.assertEqual(hotel_manager_1, hotel_manager_2)
        self.assertEqual(hotel_manager_1, hotel_manager_3)
        self.assertEqual(hotel_manager_2, hotel_manager_3)

        res_store_1 = ReservationJsonStore()
        res_store_2 = ReservationJsonStore()
        res_store_3 = ReservationJsonStore()

        self.assertEqual(res_store_1, res_store_2)
        self.assertEqual(res_store_1, res_store_3)
        self.assertEqual(res_store_2, res_store_3)

        stay_store_1 = StayJsonStore()
        stay_store_2 = StayJsonStore()
        stay_store_3 = StayJsonStore()

        self.assertEqual(stay_store_1, stay_store_2)
        self.assertEqual(stay_store_1, stay_store_3)
        self.assertEqual(stay_store_2, stay_store_3)

        checkout_store_1 = CheckoutJsonStore()
        checkout_store_2 = CheckoutJsonStore()
        checkout_store_3 = CheckoutJsonStore()

        self.assertEqual(checkout_store_1, checkout_store_2)
        self.assertEqual(checkout_store_1, checkout_store_3)
        self.assertEqual(checkout_store_2, checkout_store_3)

        credit_card = "5105105105105100"
        name_surname = "JOSE LOPEZ"
        id_card = "12345678Z"
        room_type = "SINGLE"
        arrival_date = "01/07/2024"
        num_days = 1
        phone_number = "+341234567"

        hotel_res_1 = HotelReservation(id_card=id_card,
                                              credit_card_number=credit_card,
                                              name_surname=name_surname,
                                              phone_number=phone_number,
                                              room_type=room_type,
                                              arrival=arrival_date,
                                              num_days=num_days)
        hotel_res_2 =HotelReservation(id_card=id_card,
                                              credit_card_number=credit_card,
                                              name_surname=name_surname,
                                              phone_number=phone_number,
                                              room_type=room_type,
                                              arrival=arrival_date,
                                              num_days=num_days)
        hotel_res_3 = HotelReservation(id_card=id_card,
                                              credit_card_number=credit_card,
                                              name_surname=name_surname,
                                              phone_number=phone_number,
                                              room_type=room_type,
                                              arrival=arrival_date,
                                              num_days=num_days)

        self.assertNotEqual(hotel_res_1, hotel_res_2)
        self.assertNotEqual(hotel_res_2, hotel_res_3)
        self.assertNotEqual(hotel_res_3, hotel_res_1)



if __name__ == '__main__':
    unittest.main()
