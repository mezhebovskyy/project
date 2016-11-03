class Hotel:
    def __init__(self, id, name, isavaliable):
        self.id = int(id)
        self.name = name
        self.rooms = []
        self.isavaliable = bool(isavaliable)

class Room:
    def __init__(self, id, hotelID, number, beds, price, isavaliable):
        self.id = int(id)
        self.hotelID = int(hotelID)
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
