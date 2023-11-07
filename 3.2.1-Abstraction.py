from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    @abstractmethod
    def drive(self):
        pass

# Concrete class
class Car(Vehicle):
    def drive(self):
        print(f"Driving a {self.make} {self.model} on the road!")

# Another concrete class
class Boat(Vehicle):
    def drive(self):
        print(f"Sailing a {self.make} {self.model} on the water!")

# Usage
my_car = Car("Toyota", "Corolla")
my_car.drive() # Output: Driving a Toyota Corolla on the road!

my_boat = Boat("Yamaha", "242X")
my_boat.drive() # Output: Sailing a Yamaha 242X on the water!

# Trying to instantiate an abstract class will raise an error
try:
    my_vehicle = Vehicle("Generic", "Model")
except TypeError as e:
    print(e) # Output: Can't instantiate abstract class Vehicle with abstract method drive