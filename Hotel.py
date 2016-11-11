import sqlite3 as lite
import sys
import uuid
from Models import Hotel
from Room import *
# from Order import OrderService

database = "HROdata.db"

class HotelService:
    def __init__(self, hr):
        self.listofhotels = []
        self.roomservice = RoomService()
        self.reader = hr

    def loadhotels(self):
        self.listofhotels = self.reader.loadData(database)
        for hotel in self.listofhotels:
            hotel.rooms = self.roomservice.loadRoomsForHotel(hotel.id)

    def getHotel(self, hotelnumber):
        for hotel in self.listofhotels:
            if self.listofhotels.index(hotel) == int(hotelnumber) - 1:
                return hotel

    def getHotelById(self, hotelID):
        for hotel in self.listofhotels:
            if hotel.id == hotelID:
                return hotel

    def getHotelsByStatus(self, status):
        hotels = []
        for hotel in self.listofhotels:
            if hotel.isavaliable == status:
                hotels.append(hotel)
        return hotels

    def getAllHotels(self):
        return self.listofhotels

    def addhotel(self, name, isavaliable):
        ID = uuid.uuid4()
        hotel = Hotel(ID, name, isavaliable)
        self.listofhotels.append(hotel)
        HotelReader().saveNewHotel(hotel)

    def editHotelName(self, hotelnumber, newname):
        hotel = self.getHotel(hotelnumber)
        hotel.name = newname
        HotelReader().updateHotelName(hotel, newname)

    def editHotelStatus(self, hotelnumber):
        hotel = self.getHotel(hotelnumber)
        hotel.isavaliable = not hotel.isavaliable
        HotelReader().updateHotelStatus(hotel)

    def deleteHotel(self, hotelnumber):
        hotel = self.getHotel(hotelnumber)
        HotelReader().deleteHotelFromDB(hotel.id)
        self.listofhotels.remove(hotel)

class HotelPrinter:
    def showAllHotels(self, hotels):
        print "Here is the list of all hotels: "
        index = 1
        for hotel in hotels:
            if hotel.isavaliable == True:
                status = "avaliable"
                print "%s) Hotel name - %s. Status - %s. ID - %s." % (index, hotel.name, status, hotel.id)
            else:
                status = "not avaliable"
                print "%s) Hotel name - %s. Status - %s. ID - %s." % (index, hotel.name, status, hotel.id)
            index += 1

    def showHotelsByStatus(self, hotels, status):
        if status:
            title = "avaliable"
        else:
            title = "not avaliable"
        print "Here is the list of %s hotels: " % title
        for hotel in hotels:
            print "Hotel name - %s. ID - %s." % (hotel.name, hotel.id)

class HotelReader:
    def loadData(self, database):
        array = []
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Hotels")
            rows = cursor.fetchall()
            for row in rows:
                array.append(Hotel(row["Id"], str(row["Name"]), row["Status"] == "True"))
            return array
        conn.close()

    def saveNewHotel(self, hotel):
        conn = lite.connect(database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Hotels VALUES(?, ?, ?)", (str(hotel.id), hotel.name, str(hotel.isavaliable)))
        conn.commit()
        conn.close()

    def updateHotelName(self, hotel, name):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Hotels SET Name=? WHERE Id=?", (name, str(hotel.id)))
            conn.commit()
        conn.close()

    def updateHotelStatus(self, hotel):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Hotels SET Status=? WHERE Id=?", (str(hotel.isavaliable), str(hotel.id)))
            conn.commit()
        conn.close()

    def deleteHotelFromDB(self, hotelID):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Hotels WHERE Id=?", [str(hotelID)])
            cursor.execute("DELETE FROM Rooms WHERE HotelID=?", [str(hotelID)])
            conn.commit()
        conn.close()