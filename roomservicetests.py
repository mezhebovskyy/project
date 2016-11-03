import unittest
from Hotel import HotelService
from Room import RoomService

class RoomServiceTestSuite(unittest.TestCase):
    def test_can_get_room_by_number


    def test_can_Add_New_Room(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)

        for hotel in hotelservice.listofhotels:
            for room in hotel.rooms:
                self.assertEqual(room.hotelID, hotel.id)


    def test_can_Delete_Room(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)
        roomservice.addRoom(hotel, 101, 2, 1500, True)
        roomservice.deleteRoom(hotel, 100)

        for hotel in hotelservice.listofhotels:
            self.assertEqual(len(hotel.rooms), 1)


    def test_can_Edit_Room(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)
        room = hotel.room
        roomservice.editRoom(room, 200, 2, 1500, ".")

        for hotel in hotelservice.listofhotels:
            for room in hotel.rooms:
                self.assertEqual(room.number, 200)
                self.assertEqual(room.beds, 2)
                self.assertEqual(room.price, 1500)
                self.assertEqual(room.isavaliable, True)


# class HotelServiceTestSuite(unittest.TestCase):
#     def test_can_add_new_hotel(self):
#         hotelservice = HotelService()
#
#         hotelservice.addhotel("fff", True)
#
#         self.assertEqual(len(hotelservice.listofhotels), 1)
#
#
#     def test_can_delete_hotel(self):
#         hotelservice = HotelService()
#         hotelservice.addhotel("mmm", True)
#         hotelservice.addhotel("nnn", True)
#
#         hotelservice.deleteHotel(2)
#
#         self.assertEqual(len(hotelservice.listofhotels), 1)
#         for hotel in hotelservice.listofhotels:
#             self.assertEqual(hotel.name, "mmm")
#
#
#     def test_can_Edit_Hotel_Name(self):
#         hotelservice = HotelService()
#         hotelservice.addhotel("mmm", True)
#
#         hotelservice.editHotelName(1, "ttt")
#
#         for hotel in hotelservice.listofhotels:
#             self.assertEqual(hotel.name, "ttt")
#
#
#     def test_can_Edit_Hotel_Status(self):
#         hotelservice = HotelService()
#         hotelservice.addhotel("mmm", True)
#
#         hotelservice.editHotelStatus(1)
#
#         for hotel in hotelservice.listofhotels:
#             self.assertEqual(hotel.isavaliable, False)
#
#
#     # def test_get_Hotel_By_Id(self):
#     #     hotelservice = HotelService()
#     #     hotelservice.addhotel("mmm", True)
#     #     for neededhotel in hotelservice.listofhotels:
#     #         if neededhotel.id == "1":
#     #             return neededhotel.name
#     #     hotel = hotelservice.getHotelByID(1)
#     #     self.assertTrue(neededhotel.name == hotel.name)
#
#
#     def test_can_get_Hotel_by_Number(self):
#         hotelservice = HotelService()
#         hotelservice.addhotel("mmm", True)
#         hotelservice.addhotel("vvv", True)
#         hotelservice.addhotel("nnn", False)
#
#         hotel = hotelservice.getHotel(3)
#
#         self.assertEqual(hotel.name, "nnn")
#
#
#     def test_get_Hotels_By_Status(self):
#         hotelservice = HotelService()
#         hotelservice.addhotel("mmm", True)
#         hotelservice.addhotel("vvv", True)
#         hotelservice.addhotel("nnn", False)
#
#         avaliableHotels = hotelservice.getHotelsByStatus(True)
#         notAvaliableHotels = hotelservice.getHotelsByStatus(False)
#
#         self.assertEqual(len(avaliableHotels), 2)
#         self.assertEqual(len(notAvaliableHotels), 1)
#
#
#     def test_get_All_Hotels(self):
#         hotelservice = HotelService()
#         hotelservice.addhotel("mmm", True)
#         hotelservice.addhotel("nnn", True)
#
#         hotels = hotelservice.getAllHotels()
#
#         self.assertEqual(len(hotels), 2)


if __name__ == "__main__":
    unittest.main()