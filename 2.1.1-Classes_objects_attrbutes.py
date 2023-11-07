# Defining the Car class (blueprint)
class Car:
    # Initializing the attributes for the Car class
    def __init__(self, model, price, color, build_year):
        self.model = model
        self.price = price
        self.color = color
        self.build_year = build_year

    # Method to display information about the car
    def display_info(self):
        return f"Model: {self.model}, Price: {self.price}, Color: {self.color}, Build year: {self.build_year}"

# Creating instances (objects) of the Car class

# Orange Car Object
car1 = Car(model="AAA", price="10K", color="Orange", build_year=2015)

# Blue Car Object
car2 = Car(model="BBB", price="15K", color="Blue", build_year=2018)

# Green Car Object
car3 = Car(model="CCC", price="45K", color="Green", build_year=2015)