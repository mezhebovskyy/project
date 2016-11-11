import unittest
from Hotel import HotelService
from Room import RoomService

class RoomServiceTestSuite(unittest.TestCase):
    def test_can_Get_Room_By_Number(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)
        roomservice.addRoom(hotel, 101, 2, 1500, True)
        neededroom = roomservice.getRoomByNumber(hotel, 100)

        self.assertEqual(neededroom.number, 100)


    def test_can_Get_Room_By_Id(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)
        roomservice.addRoom(hotel, 101, 2, 1500, True)
        hotels = hotelservice.getAllHotels()
        for hotel in hotelservice.listofhotels:
            for room in hotel.rooms:
                if room.number == 100:
                    roomID = room.id
        room = roomservice.getRoomById(hotels, roomID)

        self.assertEqual(room.id, roomID)


    def test_can_Get_Room_By_Status(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)
        roomservice.addRoom(hotel, 101, 2, 1500, False)
        roomservice.addRoom(hotel, 102, 3, 1200, False)
        hotels = hotelservice.getAllHotels()
        rooms = roomservice.getRoomsByStatus(hotels, False)

        self.assertEqual(len(rooms), 2)
        for room in rooms:
            self.assertEqual(room.isavaliable, False)


    def test_can_Get_Rooms_By_Hotel(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)
        roomservice.addRoom(hotel, 101, 2, 1500, False)
        rooms = roomservice.getRoomsByHotel(hotel)

        self.assertEqual(len(rooms), 2)


    def test_can_Get_All_Rooms(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotelservice.addhotel("aaa", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)
        roomservice.addRoom(hotel, 101, 2, 1500, False)
        hotel2 = hotelservice.getHotel(2)
        roomservice.addRoom(hotel2, 200, 1, 500, True)
        hotels = hotelservice.getAllHotels()
        rooms = roomservice.getAllRooms(hotels)

        self.assertEqual(len(rooms), 3)


    def test_can_Add_New_Room(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)

        for hotel in hotelservice.listofhotels:
            for room in hotel.rooms:
                self.assertEqual(room.hotelID, hotel.id)


    def test_can_Edit_Room(self):
        hotelservice = HotelService()
        roomservice = RoomService()

        hotelservice.addhotel("fff", True)
        hotel = hotelservice.getHotel(1)
        roomservice.addRoom(hotel, 100, 4, 1000, True)
        room = roomservice.getRoomByNumber(hotel, 100)
        roomservice.editRoom(room, 200, 2, 1500, ".")

        for hotel in hotelservice.listofhotels:
            for room in hotel.rooms:
                self.assertEqual(room.number, 200)
                self.assertEqual(room.beds, 2)
                self.assertEqual(room.price, 1500)
                self.assertEqual(room.isavaliable, True)


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


if __name__ == "__main__":
    unittest.main()