import uuid
from Models import Room
from Hotel import *

roomFileName = "fileRooms.csv"


class RoomService:
    def loadRoomsForHotel(self, hotelid):
        roomreader = RoomReader()
        rooms = roomreader.readfromfile(roomFileName, hotelid)
        return rooms

    def getRoomByNumber(self, hotel, roomNumber):
        for room in hotel.rooms:
            if room.number == int(roomNumber):
                return room

    def getRoomById(self, hotels, roomID):
        for hotel in hotels:
            for room in hotel.rooms:
                if room.id == int(roomID):
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

    def editRoom(self, room, newnumber, newbeds, newprice, newstatus):
        if newnumber != ".":
            room.number = newnumber
        if newbeds != ".":
            room.beds = newbeds
        if newprice != ".":
            room.price = newprice
        if newstatus != ".":
            room.isavaliable = newstatus

    def deleteRoom(self, hotel, roomNumber):
        for room in hotel.rooms:
            if room.number == int(roomNumber):
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
    def readfromfile(self, fileName, hotelid):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            id, hotelID, number, beds, price, isavaliable = line.split(",")
            if int(hotelID) == hotelid:
                array.append(Room(id, hotelID, number, beds, price, isavaliable))
        f.close()
        return array

    def saveroom(self, hotels):
        open(roomFileName, "w").close()
        f = open(roomFileName, "a")
        for hotel in hotels:
            for room in hotel.rooms:
                linetoadd = "%s,%s,%s,%s,%s,%s\n" % (room.id, room.hotelID, room.number, room.beds, room.price, room.isavaliable)
                f.write(linetoadd)
        f.flush()
        f.close()
