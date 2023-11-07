class Car:
    def __init__(self, model, max_speed):
        self.model = model
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, increase):
        """Increase current speed, not exceeding the max speed."""
        self.current_speed += increase
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        print(f"{self.model} accelerated to {self.current_speed} km/h")

    def brake(self):
        """Reset current speed to zero."""
        self.current_speed = 0
        print(f"{self.model} braked to a stop.")

# Create an instance of Car
my_car = Car("AAA", 180)

# Call the accelerate method to speed up the car
my_car.accelerate(50)
my_car.accelerate(20)

# Call the brake method to stop the car
my_car.brake()