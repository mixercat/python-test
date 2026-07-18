
class Vehicle:
    def turnOnAirConditioner(self):
        print(self.__class__.__name__, "Air Conditioner is turned on.")
        print("Successfully turned on the air conditioner.")
        print("---------------------------------------------------")

class Car(Vehicle):
    car_brand = ""
    License_Plate = ""
    model = ""
    def turnOnAirConditioner(self):
        print(self.__class__.__name__, "Air Conditioner is turned on.")
        print("Successfully turned on the air conditioner.")
        print("---------------------------------------------------")

class PickupTruck(Vehicle):
    pass

class Van(Vehicle):
    pass

class EstateCar(Vehicle):
    pass


Van1 = Van()
Van1.turnOnAirConditioner()

PickupTruck1 = PickupTruck()
PickupTruck1.turnOnAirConditioner()

EstateCar1 = EstateCar()
EstateCar1.turnOnAirConditioner()