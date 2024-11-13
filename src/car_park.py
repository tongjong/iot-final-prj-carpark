import random
from display import Display

class CarPark:
    def __init__(self,name:str, capacity: int, location: str, display: Display):
        self.name = name
        self.capacity = capacity
        self.location = location
        self.display = display
        self.plates = []
        self.temperature = random.randint(15,40)

    @classmethod
    def get_car_park(cls, name, capacity, location, display) -> 'CarPark':
        return cls(name, capacity, location, display)

    @property
    def car_park_info(self) -> str:
        return f"Welcome to {self.name} in {self.location}!  It is ready to operate."

    @property
    def available_bays(self) -> int:
        return max(self.capacity - len(self.plates), 0)

    def update_display(self, message=None) -> None:
        self.display.show(self.available_bays, self.temperature, message)


