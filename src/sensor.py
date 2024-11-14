
from car_park import CarPark
from abc import ABC,abstractmethod

from car_parking_log import Logger


class Sensor(ABC):
    def __init__(self, car_park: CarPark):
        self.car_park = car_park
        self.is_on = True
        self.detected_plate = None
        self.logger = Logger()

    @abstractmethod
    def detect_car(self):
        pass

    @abstractmethod
    def update(self):
        pass