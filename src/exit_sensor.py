import random

from src.car_park import CarPark
from src.sensor import Sensor


class ExitSensor(Sensor):
    def __init__(self, car_park: CarPark):
        super().__init__(car_park)
        self.last_detected_car = None

    def detect_car(self):
        if self.car_park.plates > 0:
            self.last_detected_car = random.choice(self.car_park.plates)
            return self.last_detected_car

    def update(self):
        if self.last_detected_car is not None:
            self.car_park.plates.remove(self.last_detected_car)

