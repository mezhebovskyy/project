import uuid
from Models import Hotel
from Room import *
# from Order import OrderService

hotelFileName = "fileHotels.csv"

class HotelService:
    def __init__(self):
        self.listofhotels = []
        self.roomservice = RoomService()
    
    def loadhotels(self):
        reader = HotelReader()
        self.listofhotels = reader.loadData(hotelFileName)
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

    def editHotelName(self, hotelnumber, newname):
        hotel = self.getHotel(hotelnumber)
        hotel.name = newname

    def editHotelStatus(self, hotelnumber):
        hotel = self.getHotel(hotelnumber)
        hotel.isavaliable = not hotel.isavaliable

    def deleteHotel(self, hotelnumber):
        hotel = self.getHotel(hotelnumber)
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
    def loadData(self, fileName):
        array = []
        f = open(fileName, "r")
        for line in f:
            line = line.replace('\n','')
            id, name, status = line.split(",")
            array.append(Hotel(id, name, status))
        f.close()
        return array

    def savehotel(self, hotels):
        open(hotelFileName, "w").close()
        f = open(hotelFileName, "a")
        for hotel in hotels:
            linetoadd = "%s,%s,%s\n" % (hotel.id, hotel.name, hotel.isavaliable)
            f.write(linetoadd)
        f.flush()
        f.close()




