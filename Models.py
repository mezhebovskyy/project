import sqlite3 as lite
import os

class Hotel:
    def __init__(self, id, name, isavaliable):
        self.id = str(id)
        self.name = name
        self.rooms = []
        self.isavaliable = bool(isavaliable)

class Room:
    def __init__(self, id, hotelID, number, beds, price, isavaliable):
        self.id = str(id)
        self.hotelID = str(hotelID)
        self.number = int(number)
        self.beds = int(beds)
        self.price = int(price)
        self.isavaliable = bool(isavaliable)

class Order:
    def __init__(self, id, roomID, hotelID, stayfrom, staytill, numberofvisitors, email):
        self.id = id
        self.roomID = roomID
        self.hotelID = hotelID
        self.stayfrom = stayfrom
        self.staytill = staytill
        self.numberofvisitors = numberofvisitors
        self.email = email

class Database:
    def isDbCreated(self):
        while True:
            if os.path.exists('HROdata.db') == False:
                conn = lite.connect('HROdata.db')
                conn.close()
            else:
                break

    def isHotelsTableCreated(self):
        conn = lite.connect('HROdata.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Hotels(Id VARCHAR (40), Name VARCHAR (255),"
                       "Status VARCHAR (5), PRIMARY KEY (Id))")
        conn.close()

    def isRoomsTableCreated(self):
        conn = lite.connect('HROdata.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Rooms(Id VARCHAR (40), HotelID VARCHAR (40), Number INT NOT NULL, "
                       "Beds INT NOT NULL, Price INT NOT NULL, Status VARCHAR (5), PRIMARY KEY (Id), "
                       "FOREIGN KEY (HotelID) REFERENCES Hotels(Id))")
        conn.close()






