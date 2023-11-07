class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__speed = 0  # Private attribute

    def accelerate(self, increase):
        if increase > 0:
            self.__speed += increase
            print(f"The {self.model} is now going {self.__speed} km/h.")

    def brake(self):
        self.__speed = 0
        print(f"The {self.model} has stopped.")

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if 0 <= speed <= 200:  # We can enforce a valid range for speed
            self.__speed = speed
        else:
            print("Speed must be between 0 and 200 km/h.")

# Usage
my_car = Car('Toyota', 'Corolla', 2020)

# Accelerate the car by 50 km/h
my_car.accelerate(50)

# The following line would raise an error, because __speed is private
# print(my_car.__speed)  # This will give an attribute error

# Use the method to safely access the speed
current_speed = my_car.get_speed()
print(f"Current speed is {current_speed} km/h")  # Output: Current speed is 50 km/h

# Attempt to directly set a new speed – this will use the setter method which has a check
my_car.set_speed(150)  # This will set the new speed if it's within the valid range