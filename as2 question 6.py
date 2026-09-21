# Base class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    # Base method to be overridden
    def move(self):
        return f"The {self.brand} is moving at {self.speed} km/h."

# Subclass for Cars
class Car(Vehicle):
    # Overriding the move method
    def move(self):
        return f"The {self.brand} car cruises smoothly down the highway at {self.speed} km/h."

# Subclass for Bikes
class Bike(Vehicle):
    # Overriding the move method
    def move(self):
        return f"The {self.brand} bike weaves through traffic at {self.speed} km/h."


# --- Demonstration ---

# Creating instances of each class
generic_vehicle = Vehicle("Generic", 40)
my_car = Car("Toyota", 120)
my_bike = Bike("Yamaha", 80)

# Calling the move method on each object
print(generic_vehicle.move())  # Output: The Generic is moving at 40 km/h.
print(my_car.move())           # Output: The Toyota car cruises smoothly down the highway at 120 km/h.
print(my_bike.move())          # Output: The Yamaha bike weaves through traffic at 80 km/h.
