from abc import ABC, abstractmethod

# abstract class

class Vehical(ABC):
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def get_details(self):
        print("Brand is ", self.brand)
        print("Model is ", self.model)
        print("Fuel type is ", self.fuel_type)
        

class Car(Vehical):
    def start_engine(self):
        print("car started")

    def stop_engine(self):
        print("Car stopped")


class Bike(Vehical):
    def start_engine(self):
        print("Bike started")

    def stop_engine(self):
        print("Bike stopped")

# v = Vehical("BMW", "camry", "Petrol")
c = Car("skoda", "camry", "Petrol")
d = Bike("BMW", "camry", "Diesel")

c.get_details()
c.start_engine()
c.stop_engine()