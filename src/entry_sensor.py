import random

from src.car_park import CarPark
from src.sensor import Sensor


class EntrySensor(Sensor):
    def __init__(self, car_park: CarPark):
        super().__init__(car_park)
        self.last_detected_car = None

    def detect_car(self):
        number = random.randint(0, 999)
        self.last_detected_car =  f"FAKE-{number:03}"
        return self.last_detected_car

    def update(self):
        if self.last_detected_car is not None:
            self.car_park.plates.append(self.last_detected_car)