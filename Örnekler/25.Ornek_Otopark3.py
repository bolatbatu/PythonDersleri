import datetime
class Car:
    def __init__(self, brand, model, color, plate):
        self.brand = brand
        self.model = model
        self.color = color
        self.plate = plate
        self.giris = datetime.datetime.now()
        self.cikis = None
        self.ücret = None
class ParkingSpot:
    def __init__(self):
        self.car = None

    def is_empty(self):
        return self.car is None

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.spots = [ParkingSpot() for i in range(capacity)]

    def park(self, car):
        for spot in self.spots:
            if spot.is_empty():
                spot.car = car
                return True
        return False

    def retrieve(self, plate):
        for spot in self.spots:
            if spot.car and spot.car.plate == plate:
                spot.car.cikis = datetime.datetime.now()
                spot.car.ücret = ((spot.car.cikis - spot.car.giris).total_seconds()*20)
                car = spot.car.ücret
                spot.car = None
                return car
        return car

parking_lot = ParkingLot(50)

while True:
    command = input("Enter a command (park, retrieve, exit): ")
    if command == "park":
        brand = input("Enter car brand: ")
        model = input("Enter car model: ")
        color = input("Enter car color: ")
        plate = input("Enter car plate: ")
        car = Car(brand, model, color, plate)
        if parking_lot.park(car):
            print("Car parked successfully.")
        else:
            print("Parking lot is full.")
    elif command == "retrieve":
        plate = input("Enter car plate: ")
        car = parking_lot.retrieve(plate)
        if car:
            print("Car retrieved successfully.")
            print("Ücretiniz: ", car,"TL")
        else:
            print("Car not found.")
    elif command == "exit":
        break
    else:
        print("Invalid command.")
