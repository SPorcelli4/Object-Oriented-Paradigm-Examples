class Vehicle:
    def drive(self):
        raise NotImplementedError("You must implement the drive method.")

class Car(Vehicle):
    def drive(self):
        print("The car is driving on the road.")

class Boat(Vehicle):
    def drive(self):
        print("The boat is sailing on the water.")

class Airplane(Vehicle):
    def drive(self):
        print("The airplane is flying in the air.")

# Function that uses polymorphism
def start_journey(vehicle):
    vehicle.drive()

# Create instances of the subclasses
my_car = Car()
my_boat = Boat()
my_airplane = Airplane()

# Call the same function with different objects
start_journey(my_car)        # Output: The car is driving on the road.
start_journey(my_boat)       # Output: The boat is sailing on the water.
start_journey(my_airplane)   # Output: The airplane is flying in the air.