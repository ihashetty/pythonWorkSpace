"""OOPS car code"""


class Car:

    """Car class"""
    def __init__(self, brand, color):
        self.brand = brand  # Attribute
        self.color = color  # Attribute

    def drive(self):

        """Drive function"""
        print(f"The {self.color} {self.brand} is now driving!")


my_car = Car("Toyota", "Red")

print(my_car.brand)
print(my_car.color)

my_car.drive()
