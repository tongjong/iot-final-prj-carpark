import random

from display import Display

class CarPark:
    def __init__(self,name:str, capacity: int, location: str, display: Display):
        self.name = name
        self.capacity = capacity
        self.location = location
        self.display = display
        self.plates = []

    @classmethod
    def get_car_park(cls, name, capacity, location, display):
        return cls(name, capacity, location, display)




