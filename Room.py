import sqlite3 as lite
import sys
import uuid
from Models import Room
from Hotel import *

database = "HROdata.db"


class RoomService:
    def loadRoomsForHotel(self, hotelid):
        roomreader = RoomReader()
        rooms = roomreader.loadRooms(database, hotelid)
        return rooms

    def getRoomByNumber(self, hotel, roomNumber):
        for room in hotel.rooms:
            if room.number == int(roomNumber):
                return room

    def getRoomById(self, hotels, roomID):
        for hotel in hotels:
            for room in hotel.rooms:
                if room.id == str(roomID):
                    return room

    def getRoomsByStatus(self, hotels, status):
        rooms = []
        for hotel in hotels:
            for room in hotel.rooms:
                if room.isavaliable == bool(status):
                    rooms.append(room)
        return rooms

    def getRoomsByHotel(self, hotel):
        rooms = hotel.rooms
        return rooms

    def getAllRooms(self, hotels):
        rooms = []
        for hotel in hotels:
            for room in hotel.rooms:
                rooms.append(room)
        return rooms

    def addRoom(self, hotel, number, beds, price, isavaliable):
        ID = uuid.uuid4()
        hotelid = hotel.id
        hotel.rooms.append(Room(ID, hotelid, number, beds, price, isavaliable))
        for room in hotel.rooms:
            if room.id == str(ID):
                RoomReader().saveRoom(room)

    def editRoom(self, room, newnumber, newbeds, newprice, newstatus):
        if newnumber != ".":
            room.number = newnumber
        if newbeds != ".":
            room.beds = newbeds
        if newprice != ".":
            room.price = newprice
        if newstatus != ".":
            room.isavaliable = newstatus
        RoomReader().updateRoom(room)

    def deleteRoom(self, hotel, roomNumber):
        for room in hotel.rooms:
            if room.number == int(roomNumber):
                RoomReader().deleteRoomFromDB(room.id)
                hotel.rooms.remove(room)


class RoomPrinter:
    def showAllRooms(self, hotels):
        print "Here is the list of all rooms: "
        index = 1
        for hotel in hotels:
            for room in hotel.rooms:
                if room.isavaliable == True:
                    status = "avaliable"
                    print ("%s) Hotel name - %s. Room number - %s. Number of beds - %s. Price - %s. Status - %s."
                           % (index, hotel.name, room.number, room.beds, room.price, status))
                else:
                    status = "not avaliable"
                    print ("%s) Hotel name - %s. Room number - %s. Number of beds - %s. Price - %s. Status - %s."
                           % (index, hotel.name, room.number, room.beds, room.price, status))
                index += 1

    def showRoomsByHotel(self, hotel):
        for room in hotel.rooms:
            if room.isavaliable == True:
                status = "avaliable"
                print "Room number - %s. Status - %s. Number of beds - %s. Price - %s" % (room.number, status, room.beds, room.price)
            else:
                status = "not avaliable"
                print "Room number - %s. Status - %s. Number of beds - %s. Price - %s" % (room.number, status, room.beds, room.price)

    def showRoomsByStatus(self, hotels, status):
        if status:
            title = "avaliable"
        else:
            title = "not avaliable"
        print "Here is the list of %s rooms: " % title
        for hotel in hotels:
            for room in hotel.rooms:
                if room.isavaliable == status:
                    print ("%s) Hotel name - %s. Room number - %s. Number of beds - %s. Price - %s."
                           % (index, hotel.name, room.number, room.beds, room.price))


class RoomReader:
    def loadRooms(self, database, hotelid):
        array = []
        conn = lite.connect(database)
        with conn:
            conn.row_factory = lite.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Rooms")
            rows = cursor.fetchall()
            for row in rows:
                if str(row["HotelID"]) == hotelid:
                    if row["Status"] == "True":
                        array.append(Room(row["Id"], row["HotelID"], row["Number"], row["Beds"], row["Price"], True))
                    if row["Status"] == "False":
                        array.append(Room(row["Id"], row["HotelID"], row["Number"], row["Beds"], row["Price"], False))
            return array
        conn.close()

    def saveRoom(self, room):
        conn = lite.connect(database)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Rooms VALUES(?, ?, ?, ?, ?, ?)", (str(room.id), str(room.hotelID),
                                                                      room.number, room.beds, room.price, str(room.isavaliable)))
        conn.commit()
        conn.close()

    def updateRoom(self, room):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Rooms SET Number=?, Beds=?, Price=?, Status=? WHERE Id=?", (room.number, room.beds,
                                                                                               str(room.price), str(room.isavaliable), str(room.id)))
            conn.commit()
        conn.close()

    def deleteRoomFromDB(self, ID):
        conn = lite.connect(database)
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Rooms WHERE Id=?", [str(ID)])
            conn.commit()
        conn.close()
