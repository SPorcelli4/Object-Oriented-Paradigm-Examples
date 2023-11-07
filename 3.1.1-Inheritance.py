# Base class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
    
    def accelerate(self, increase):
        self.speed += increase
        print(f"The {self.model} is now going {self.speed} km/h.")
    
    def brake(self):
        self.speed = 0
        print(f"The {self.model} has stopped.")

# Derived class inheriting Car class
class SportsCar(Car):
    def __init__(self, make, model, year, turbo):
        super().__init__(make, model, year)
        self.turbo = turbo
    
    def activate_turbo(self):
        if self.turbo:
            self.speed *= 1.5
            print(f"Turbo activated! The {self.model} speed is now {self.speed} km/h.")
        else:
            print("This model does not have a turbo feature.")

# Usage
my_sports_car = SportsCar('Mazda', 'RX-7', 1999, True)

# Inherited methods can be used by instances of the derived class
my_sports_car.accelerate(100) # The RX-7 is now going 100 km/h.

# Methods from the derived class can also be used
my_sports_car.activate_turbo() # Turbo activated! The RX-7 speed is now 150 km/h.

# The brake method is also inherited from the base class
my_sports_car.brake() # The RX-7 has stopped.