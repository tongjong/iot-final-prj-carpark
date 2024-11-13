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

    @property
    def car_park_info(self) -> str:
        return f"Welcome to {self.name} in {self.location}!  It is ready to operate."

    @property
    def available_bays(self) -> int:
        return max(self.capacity - len(self.plates), 0)

    def update_display(self, message=None) -> None:
        self.display.available_bays = self.available_bays
        self.display.temperature = random.randint(10,40)
        if message is not None:
            self.display.message = message
        self.display.show()


